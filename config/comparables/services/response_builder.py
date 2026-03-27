# def build_final_response(query: str, parsed_query: dict, column_schema: list, rows: list) -> dict:
#     return {
#         "title": f"Results for: {query}",
#         "query_plan": parsed_query,
#         "columns": column_schema,
#         "rows": rows
#     }
from typing import Dict, List


TEXT_FALLBACKS = {
    "personal_question": "This query is personal and should not generate a property table.",
    "knowledge_question": "This query is general knowledge and should be answered in text form, not as a table.",
    "greeting": "This is a greeting, so no data table is needed.",
    "unsupported": "This query is outside the supported real-estate table workflow.",
    "generic": "No table is required for this query.",
}


def build_text_response(query: str, parsed_query: Dict) -> Dict:
    intent = parsed_query.get("intent", "unsupported")
    answer = (
        parsed_query.get("reasoning_summary")
        or TEXT_FALLBACKS.get(intent, TEXT_FALLBACKS["generic"])
    )

    return {
        "title": f"Answer for: {query}",
        "response_type": "text",
        "query_plan": parsed_query,
        "context": parsed_query.get("context"),
        "visible_columns": [],
        "answer": answer,
        "columns": [],
        "rows": [],
    }


def build_table_response(
    query: str,
    parsed_query: Dict,
    column_schema: List[Dict],
    rows: List[Dict],
) -> Dict:
    return {
        "title": f"Results for: {query}",
        "response_type": "table",
        "query_plan": parsed_query,
        "context": parsed_query.get("context"),
        "visible_columns": [col.get("key") for col in column_schema],
        "columns": column_schema,
        "rows": rows,
    }