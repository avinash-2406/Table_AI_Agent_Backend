# from typing import TypedDict, List, Dict, Any
# from langgraph.graph import StateGraph, START, END

# from comparables.services.query_parser import parse_query_to_plan
# from comparables.services.column_registry import ATTRIBUTE_GROUPS, MASTER_COLUMN_REGISTRY
# from comparables.services.comparable_fetcher import fetch_comparables
# from comparables.services.scoring import score_rows
# from comparables.services.response_builder import build_final_response

# class TableAgentState(TypedDict, total=False):
#     user_query: str
#     parsed_query: Dict[str, Any]
#     selected_columns: List[str]
#     column_schema: List[Dict[str, Any]]
#     raw_rows: List[Dict[str, Any]]
#     ranked_rows: List[Dict[str, Any]]
#     final_response: Dict[str, Any]

# def parse_query_node(state: TableAgentState):
#     plan = parse_query_to_plan(state["user_query"])
#     return {"parsed_query": plan}

# def build_schema_node(state: TableAgentState):
#     groups = state["parsed_query"]["attribute_groups"]

#     selected_columns = []
#     for group in groups:
#         selected_columns.extend(ATTRIBUTE_GROUPS.get(group, []))

#     # remove duplicates but keep order
#     seen = set()
#     selected_columns = [c for c in selected_columns if not (c in seen or seen.add(c))]

#     schema = []
#     for col in selected_columns:
#         item = MASTER_COLUMN_REGISTRY[col].copy()
#         item["key"] = col
#         schema.append(item)

#     return {
#         "selected_columns": selected_columns,
#         "column_schema": schema
#     }

# def fetch_rows_node(state: TableAgentState):
#     rows = fetch_comparables(
#         parsed_query=state["parsed_query"],
#         selected_columns=state["selected_columns"]
#     )
#     return {"raw_rows": rows}

# def score_rows_node(state: TableAgentState):
#     ranked = score_rows(
#         rows=state["raw_rows"],
#         comparison_mode=state["parsed_query"].get("comparison_mode", "generic")
#     )
#     return {"ranked_rows": ranked}

# def build_response_node(state: TableAgentState):
#     response = build_final_response(
#         query=state["user_query"],
#         parsed_query=state["parsed_query"],
#         column_schema=state["column_schema"],
#         rows=state["ranked_rows"]
#     )
#     return {"final_response": response}

# graph_builder = StateGraph(TableAgentState)
# graph_builder.add_node("parse_query", parse_query_node)
# graph_builder.add_node("build_schema", build_schema_node)
# graph_builder.add_node("fetch_rows", fetch_rows_node)
# graph_builder.add_node("score_rows", score_rows_node)
# graph_builder.add_node("build_response", build_response_node)

# graph_builder.add_edge(START, "parse_query")
# graph_builder.add_edge("parse_query", "build_schema")
# graph_builder.add_edge("build_schema", "fetch_rows")
# graph_builder.add_edge("fetch_rows", "score_rows")
# graph_builder.add_edge("score_rows", "build_response")
# graph_builder.add_edge("build_response", END)

# table_agent_graph = graph_builder.compile()


from typing import TypedDict, List, Dict, Any
from langgraph.graph import StateGraph, START, END

from comparables.services.query_parser import parse_query_to_plan
from comparables.services.column_registry import (
    MASTER_COLUMN_REGISTRY,
    DEFAULT_BASE_COLUMNS,
    METRIC_DEPENDENCIES,
)
from comparables.services.comparable_fetcher import fetch_comparables
from comparables.services.scoring import score_rows
from comparables.services.response_builder import build_final_response


class TableAgentState(TypedDict, total=False):
    user_query: str
    parsed_query: Dict[str, Any]
    discovered_concepts: List[str]
    selected_columns: List[str]
    missing_columns: List[str]
    column_schema: List[Dict[str, Any]]
    raw_rows: List[Dict[str, Any]]
    ranked_rows: List[Dict[str, Any]]
    final_response: Dict[str, Any]


def parse_query_node(state: TableAgentState):
    plan = parse_query_to_plan(state["user_query"])
    return {"parsed_query": plan}


def discover_factors_node(state: TableAgentState):
    parsed = state["parsed_query"]
    target_metric = parsed.get("target_metric", "generic")
    factors = parsed.get("factor_hypotheses", []) or []

    concepts = list(factors)

    dependency_block = METRIC_DEPENDENCIES.get(target_metric, {})
    concepts.extend(dependency_block.get("required_concepts", []))
    concepts.extend(dependency_block.get("important_concepts", []))

    seen = set()
    concepts = [c for c in concepts if c and not (c.lower() in seen or seen.add(c.lower()))]

    return {"discovered_concepts": concepts}


def _column_match_score(column_key: str, meta: Dict[str, Any], concepts: List[str], target_metric: str) -> int:
    score = 0

    haystack = " ".join(
        [
            column_key,
            meta.get("label", ""),
            meta.get("description", ""),
            " ".join(meta.get("synonyms", [])),
            " ".join(meta.get("concept_tags", [])),
        ]
    ).lower()

    for concept in concepts:
        c = concept.lower().strip()
        if not c:
            continue
        if c in haystack:
            score += 5

        for token in c.split():
            if token in haystack:
                score += 1

    if target_metric in meta.get("required_for_metrics", []):
        score += 10

    if target_metric in meta.get("preferred_for_metrics", []):
        score += 5

    return score


def ground_columns_node(state: TableAgentState):
    parsed = state["parsed_query"]
    target_metric = parsed.get("target_metric", "generic")
    concepts = state.get("discovered_concepts", [])

    scored_candidates = []
    for col_key, meta in MASTER_COLUMN_REGISTRY.items():
        score = _column_match_score(col_key, meta, concepts, target_metric)
        if score > 0:
            scored_candidates.append((col_key, score))

    scored_candidates.sort(key=lambda x: x[1], reverse=True)

    selected_columns = list(DEFAULT_BASE_COLUMNS)
    for col_key, _ in scored_candidates:
        if col_key not in selected_columns:
            selected_columns.append(col_key)

    # Always keep ranking column
    if "similarity_score" not in selected_columns:
        selected_columns.append("similarity_score")

    # Limit width for frontend stability
    selected_columns = selected_columns[:12]

    return {"selected_columns": selected_columns}


def validate_plan_node(state: TableAgentState):
    selected_columns = state.get("selected_columns", [])
    available_keys = set(MASTER_COLUMN_REGISTRY.keys())

    valid_columns = [c for c in selected_columns if c in available_keys]
    missing_columns = [c for c in selected_columns if c not in available_keys]

    schema = []
    for col in valid_columns:
        item = MASTER_COLUMN_REGISTRY[col].copy()
        item["key"] = col
        schema.append(item)

    return {
        "selected_columns": valid_columns,
        "missing_columns": missing_columns,
        "column_schema": schema,
    }


def fetch_rows_node(state: TableAgentState):
    rows = fetch_comparables(
        parsed_query=state["parsed_query"],
        selected_columns=state["selected_columns"],
    )
    return {"raw_rows": rows}


def score_rows_node(state: TableAgentState):
    ranked = score_rows(
        rows=state["raw_rows"],
        parsed_query=state["parsed_query"],
    )
    return {"ranked_rows": ranked}


def build_response_node(state: TableAgentState):
    response = build_final_response(
        query=state["user_query"],
        parsed_query=state["parsed_query"],
        discovered_concepts=state.get("discovered_concepts", []),
        selected_columns=state.get("selected_columns", []),
        missing_columns=state.get("missing_columns", []),
        column_schema=state.get("column_schema", []),
        rows=state.get("ranked_rows", []),
    )
    return {"final_response": response}


graph_builder = StateGraph(TableAgentState)

graph_builder.add_node("parse_query", parse_query_node)
graph_builder.add_node("discover_factors", discover_factors_node)
graph_builder.add_node("ground_columns", ground_columns_node)
graph_builder.add_node("validate_plan", validate_plan_node)
graph_builder.add_node("fetch_rows", fetch_rows_node)
graph_builder.add_node("score_rows", score_rows_node)
graph_builder.add_node("build_response", build_response_node)

graph_builder.add_edge(START, "parse_query")
graph_builder.add_edge("parse_query", "discover_factors")
graph_builder.add_edge("discover_factors", "ground_columns")
graph_builder.add_edge("ground_columns", "validate_plan")
graph_builder.add_edge("validate_plan", "fetch_rows")
graph_builder.add_edge("fetch_rows", "score_rows")
graph_builder.add_edge("score_rows", "build_response")
graph_builder.add_edge("build_response", END)

table_agent_graph = graph_builder.compile()