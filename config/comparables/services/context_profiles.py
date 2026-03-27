MAX_VISIBLE_COLUMNS = 9

CONTEXT_COLUMN_PROFILES = {
    "living_quality": [
        "project_name",
        "location_name",
        "amenities_score",
        "walkability_score",
        "green_area_score",
        "distance_to_it_hub",
        "distance_to_school",
        "distance_to_hospital",
        "lifestyle_score",
    ],

    "investment": [
        "project_name",
        "location_name",
        "price_per_sqft",
        "rental_yield_percent",
        "capital_appreciation_rate",
        "price_growth_yoy",
        "absorption_rate",
        "investment_score",
        "similarity_score",
    ],

    "connectivity": [
        "project_name",
        "location_name",
        "distance_to_it_hub",
        "distance_to_metro",
        "distance_to_highway",
        "travel_time_cbd_min",
        "connectivity_score",
        "similarity_score",
    ],

    "developer_quality": [
        "project_name",
        "developer_name",
        "developer_rating",
        "project_completion_rate",
        "delay_history_score",
        "construction_quality_score",
        "brand_value_score",
        "similarity_score",
    ],

    "generic_real_estate": [
        "project_name",
        "location_name",
        "property_type",
        "bhk_type",
        "unit_area_sqft",
        "price_per_sqft",
        "possession_status",
        "similarity_score",
    ],
}