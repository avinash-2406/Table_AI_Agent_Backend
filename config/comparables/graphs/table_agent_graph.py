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

from langgraph.graph import END, START, StateGraph

from comparables.services.comparable_fetcher import fetch_comparables
from comparables.services.query_parser import parse_query_to_plan
from comparables.services.response_builder import build_table_response, build_text_response
from comparables.services.scoring import score_rows
from comparables.services.context_profiles import CONTEXT_COLUMN_PROFILES


class TableAgentState(TypedDict, total=False):
    user_query: str
    parsed_query: Dict[str, Any]
    selected_columns: List[str]
    column_schema: List[Dict[str, Any]]
    raw_rows: List[Dict[str, Any]]
    ranked_rows: List[Dict[str, Any]]
    final_response: Dict[str, Any]


# =========================
# STEP 1 → PARSE QUERY
# =========================
def parse_query_node(state: TableAgentState):
    plan = parse_query_to_plan(state["user_query"])
    return {"parsed_query": plan}


# =========================
# STEP 2 → ROUTING
# =========================
def route_after_parse(state: TableAgentState):
    if state["parsed_query"].get("response_type") == "table":
        return "build_schema"
    return "build_text_response"


# =========================
# STEP 3 → BUILD SCHEMA (🔥 MAIN FIX)
# =========================
def build_schema_node(state: TableAgentState):

    context = state["parsed_query"].get("context", "generic_real_estate")

    # 👉 ONLY ONE CONTEXT → NOT GROUPS
    selected_columns = CONTEXT_COLUMN_PROFILES.get(
        context,
        CONTEXT_COLUMN_PROFILES["generic_real_estate"]
    )

    # limit max columns
    selected_columns = selected_columns[:9]

    # build schema
    from comparables.services.column_registry import MASTER_COLUMN_REGISTRY

    schema = []
    for col in selected_columns:
        if col in MASTER_COLUMN_REGISTRY:
            item = MASTER_COLUMN_REGISTRY[col].copy()
            item["key"] = col
            schema.append(item)

    return {
        "selected_columns": selected_columns,
        "column_schema": schema
    }


# =========================
# STEP 4 → FETCH DATA
# =========================
def fetch_rows_node(state: TableAgentState):
    rows = fetch_comparables(
        parsed_query=state["parsed_query"],
        selected_columns=state["selected_columns"],
    )
    return {"raw_rows": rows}


# =========================
# STEP 5 → SCORING
# =========================
def score_rows_node(state: TableAgentState):
    ranked = score_rows(
        rows=state.get("raw_rows", []),
        comparison_mode=state["parsed_query"].get("context", "generic"),
    )
    return {"ranked_rows": ranked}


# =========================
# STEP 6 → RESPONSE
# =========================
def build_table_response_node(state: TableAgentState):
    response = build_table_response(
        query=state["user_query"],
        parsed_query=state["parsed_query"],
        column_schema=state.get("column_schema", []),
        rows=state.get("ranked_rows", []),
    )
    return {"final_response": response}


def build_text_response_node(state: TableAgentState):
    response = build_text_response(
        query=state["user_query"],
        parsed_query=state["parsed_query"],
    )
    return {"final_response": response}


# =========================
# GRAPH BUILDING
# =========================
graph_builder = StateGraph(TableAgentState)

graph_builder.add_node("parse_query", parse_query_node)
graph_builder.add_node("build_schema", build_schema_node)
graph_builder.add_node("fetch_rows", fetch_rows_node)
graph_builder.add_node("score_rows", score_rows_node)
graph_builder.add_node("build_table_response", build_table_response_node)
graph_builder.add_node("build_text_response", build_text_response_node)

graph_builder.add_edge(START, "parse_query")

graph_builder.add_conditional_edges("parse_query", route_after_parse)

graph_builder.add_edge("build_schema", "fetch_rows")
graph_builder.add_edge("fetch_rows", "score_rows")
graph_builder.add_edge("score_rows", "build_table_response")

graph_builder.add_edge("build_table_response", END)
graph_builder.add_edge("build_text_response", END)

table_agent_graph = graph_builder.compile()