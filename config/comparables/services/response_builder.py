def build_final_response(query: str, parsed_query: dict, column_schema: list, rows: list) -> dict:
    return {
        "title": f"Results for: {query}",
        "query_plan": parsed_query,
        "columns": column_schema,
        "rows": rows
    }