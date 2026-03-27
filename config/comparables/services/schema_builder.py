from comparables.services.context_profiles import CONTEXT_COLUMN_PROFILES, MAX_VISIBLE_COLUMNS
from comparables.services.column_registry import MASTER_COLUMN_REGISTRY

def build_schema(query: str, parsed_query: dict):
    context = parsed_query.get("context", "generic_real_estate")

    columns = CONTEXT_COLUMN_PROFILES.get(context, CONTEXT_COLUMN_PROFILES["generic_real_estate"])

    # LIMIT COLUMNS
    columns = columns[:MAX_VISIBLE_COLUMNS]

    schema = []
    for col in columns:
        if col in MASTER_COLUMN_REGISTRY:
            item = MASTER_COLUMN_REGISTRY[col].copy()
            item["key"] = col
            schema.append(item)

    return {
        "selected_columns": columns,
        "column_schema": schema
    }