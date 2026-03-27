# def build_final_response(query: str, parsed_query: dict, column_schema: list, rows: list) -> dict:
#     return {
#         "title": f"Results for: {query}",
#         "query_plan": parsed_query,
#         "columns": column_schema,
#         "rows": rows
#     }


from typing import Dict, List


def build_final_response(
    query: str,
    parsed_query: Dict,
    discovered_concepts: List[str],
    selected_columns: List[str],
    missing_columns: List[str],
    column_schema: List[Dict],
    rows: List[Dict],
) -> Dict:
    warnings = []

    if missing_columns:
        warnings.append(
            f"Some selected columns were not found in registry: {', '.join(missing_columns)}"
        )

    if not rows:
        warnings.append("No rows matched the current query plan or filters.")

    return {
        "title": f"Results for: {query}",
        "response_type": "table",
        "query_plan": parsed_query,
        "agent_plan": {
            "discovered_concepts": discovered_concepts,
            "selected_columns": selected_columns,
            "missing_columns": missing_columns,
            "warnings": warnings,
        },
        "columns": column_schema,
        "rows": rows,
    }