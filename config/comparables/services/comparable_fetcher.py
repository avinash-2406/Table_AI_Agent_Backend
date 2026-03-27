# def fetch_comparables(parsed_query: dict, selected_columns: list) -> list:
#     sample = [
#         {
#             "project": "Project A",
#             "location": "Baner",
#             "config": "3 BHK",
#             "area_sqft": 1400,
#             "rate_sqft": 10500,
#             "transaction_date": "2024-01-01",
#             "rental_yield": 0.03,
#             "amenities_score": "9/10",
#             "developer_grade": "A",
#             "distance_to_it_hub": 3.5,
#             "safety_score": 8.8,
#         },
#         {
#             "project": "Project B",
#             "location": "Balewadi",
#             "config": "3 BHK",
#             "area_sqft": 1450,
#             "rate_sqft": 10200,
#             "transaction_date": "2024-02-01",
#             "rental_yield": 0.028,
#             "amenities_score": "8/10",
#             "developer_grade": "A",
#             "distance_to_it_hub": 2.5,
#             "safety_score": 8.5,
#         },
#     ]

#     trimmed_rows = []
#     for row in sample:
#         trimmed = {k: row.get(k) for k in selected_columns if k in row}
#         trimmed_rows.append(trimmed)

#     return trimmed_rows


from typing import Dict, List


def fetch_comparables(parsed_query: Dict, selected_columns: List[str]) -> List[Dict]:
    """
    Temporary dynamic mock fetcher.

    Later you should replace this with:
    - SQL builder
    - ORM query
    - dynamic column selection
    - filter-based retrieval
    """

    sample = [
        {
            "project": "Project A",
            "location": "Baner",
            "config": "3 BHK",
            "area_sqft": 1400,
            "rate_sqft": 10500,
            "transaction_date": "2024-01-01",
            "rental_yield": 0.030,
            "amenities_score": 9,
            "developer_grade": "A",
            "distance_to_it_hub": 3.5,
            "safety_score": 8.8,
            "land_cost": 25000000,
            "construction_cost": 42000000,
            "finance_cost": 6000000,
            "sales_velocity": 18,
            "cash_flow_period": 24,
            "exit_value": 90000000,
            "approval_delay": 2,
        },
        {
            "project": "Project B",
            "location": "Balewadi",
            "config": "3 BHK",
            "area_sqft": 1450,
            "rate_sqft": 10200,
            "transaction_date": "2024-02-01",
            "rental_yield": 0.028,
            "amenities_score": 8,
            "developer_grade": "A",
            "distance_to_it_hub": 2.5,
            "safety_score": 8.5,
            "land_cost": 24000000,
            "construction_cost": 40000000,
            "finance_cost": 5500000,
            "sales_velocity": 20,
            "cash_flow_period": 22,
            "exit_value": 88000000,
            "approval_delay": 1,
        },
        {
            "project": "Project C",
            "location": "Hinjewadi",
            "config": "2 BHK",
            "area_sqft": 980,
            "rate_sqft": 9800,
            "transaction_date": "2024-03-10",
            "rental_yield": 0.032,
            "amenities_score": 8,
            "developer_grade": "B+",
            "distance_to_it_hub": 1.5,
            "safety_score": 8.0,
            "land_cost": 20000000,
            "construction_cost": 36000000,
            "finance_cost": 5000000,
            "sales_velocity": 24,
            "cash_flow_period": 20,
            "exit_value": 82000000,
            "approval_delay": 1,
        },
    ]

    filters = parsed_query.get("filters", {}) or {}
    location_filter = str(filters.get("location", "")).strip().lower()
    config_filter = str(filters.get("config", "")).strip().lower()

    filtered_rows = []
    for row in sample:
        if location_filter and location_filter not in str(row.get("location", "")).lower():
            continue
        if config_filter and config_filter not in str(row.get("config", "")).lower():
            continue
        filtered_rows.append(row)

    trimmed_rows = []
    for row in filtered_rows:
        trimmed = {k: row.get(k) for k in selected_columns if k in row}
        trimmed_rows.append(trimmed)

    return trimmed_rows