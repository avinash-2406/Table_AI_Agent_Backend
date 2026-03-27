MASTER_COLUMN_REGISTRY = {
    "project": {"label": "Project", "type": "text"},
    "location": {"label": "Location", "type": "text"},
    "config": {"label": "Config", "type": "text"},
    "area_sqft": {"label": "Area (sq ft)", "type": "number"},
    "rate_sqft": {"label": "₹/sq ft", "type": "currency"},
    "transaction_date": {"label": "Transaction Date", "type": "date"},
    "rental_yield": {"label": "Rental Yield", "type": "percent"},
    "amenities_score": {"label": "Amenities Score", "type": "text"},
    "developer_grade": {"label": "Developer Grade", "type": "text"},
    "distance_to_it_hub": {"label": "Distance to IT Hub", "type": "number"},
    "safety_score": {"label": "Safety Score", "type": "number"},
    "similarity_score": {"label": "Similarity Score", "type": "number"},
}

ATTRIBUTE_GROUPS = {
    "identity": ["project", "location", "config", "area_sqft"],
    "investment": ["rate_sqft", "transaction_date", "rental_yield"],
    "livability": ["amenities_score", "safety_score"],
    "connectivity": ["distance_to_it_hub"],
    "developer_quality": ["developer_grade"],
    "ranking": ["similarity_score"],
}
# MASTER_COLUMN_REGISTRY = {
#     # -------- Identity --------
#     "project_name": {"label": "Project", "type": "text"},
#     "location_name": {"label": "Location", "type": "text"},
#     "micromarket": {"label": "Micromarket", "type": "text"},
#     "city_name": {"label": "City", "type": "text"},
#     "developer_name": {"label": "Developer", "type": "text"},
#     "property_type": {"label": "Property Type", "type": "text"},
#     "bhk_type": {"label": "BHK", "type": "text"},
#     "unit_area_sqft": {"label": "Area (sq ft)", "type": "number"},
#     "possession_status": {"label": "Possession Status", "type": "text"},

#     # -------- Livability --------
#     "amenities_score": {"label": "Amenities Score", "type": "number"},
#     "safety_score": {"label": "Safety Score", "type": "number"},
#     "walkability_score": {"label": "Walkability Score", "type": "number"},
#     "green_area_score": {"label": "Green Area Score", "type": "number"},
#     "density_score": {"label": "Density Score", "type": "number"},
#     "lifestyle_score": {"label": "Lifestyle Score", "type": "number"},

#     # -------- Connectivity --------
#     "distance_to_it_hub": {"label": "Distance to IT Hub (km)", "type": "number"},
#     "distance_to_metro": {"label": "Distance to Metro (km)", "type": "number"},
#     "distance_to_highway": {"label": "Distance to Highway (km)", "type": "number"},
#     "travel_time_cbd_min": {"label": "Travel Time to CBD (min)", "type": "number"},
#     "connectivity_score": {"label": "Connectivity Score", "type": "number"},

#     # -------- Social Infrastructure --------
#     "distance_to_school": {"label": "Distance to School (km)", "type": "number"},
#     "distance_to_hospital": {"label": "Distance to Hospital (km)", "type": "number"},
#     "distance_to_mall": {"label": "Distance to Mall (km)", "type": "number"},
#     "social_infra_score": {"label": "Social Infra Score", "type": "number"},

#     # -------- Investment --------
#     "price_per_sqft": {"label": "Price Per Sq Ft", "type": "currency"},
#     "rental_yield_percent": {"label": "Rental Yield (%)", "type": "percent"},
#     "capital_appreciation_rate": {"label": "Capital Appreciation Rate", "type": "percent"},
#     "price_growth_yoy": {"label": "Price Growth YoY (%)", "type": "percent"},
#     "absorption_rate": {"label": "Absorption Rate", "type": "number"},
#     "demand_index": {"label": "Demand Index", "type": "number"},
#     "investment_score": {"label": "Investment Score", "type": "number"},

#     # -------- Developer Quality --------
#     "developer_rating": {"label": "Developer Rating", "type": "number"},
#     "project_completion_rate": {"label": "Project Completion Rate", "type": "number"},
#     "delay_history_score": {"label": "Delay History Score", "type": "number"},
#     "construction_quality_score": {"label": "Construction Quality Score", "type": "number"},
#     "brand_value_score": {"label": "Brand Value Score", "type": "number"},

#     # -------- Project Configuration --------
#     "total_units": {"label": "Total Units", "type": "number"},
#     "units_available": {"label": "Units Available", "type": "number"},
#     "floor_count": {"label": "Floor Count", "type": "number"},
#     "parking_ratio": {"label": "Parking Ratio", "type": "number"},
#     "unit_mix_score": {"label": "Unit Mix Score", "type": "number"},

#     # -------- Legal Compliance --------
#     "rera_status": {"label": "RERA Status", "type": "text"},
#     "approval_status": {"label": "Approval Status", "type": "text"},
#     "land_title_clearance": {"label": "Land Title Clearance", "type": "text"},
#     "compliance_score": {"label": "Compliance Score", "type": "number"},

#     # -------- Financials --------
#     "total_cost": {"label": "Total Cost", "type": "currency"},
#     "base_price": {"label": "Base Price", "type": "currency"},
#     "additional_charges": {"label": "Additional Charges", "type": "currency"},
#     "maintenance_cost": {"label": "Maintenance Cost", "type": "currency"},
#     "cost_efficiency_score": {"label": "Cost Efficiency Score", "type": "number"},

#     # -------- Future Growth --------
#     "upcoming_infra_score": {"label": "Upcoming Infra Score", "type": "number"},
#     "metro_impact_score": {"label": "Metro Impact Score", "type": "number"},
#     "road_widening_impact": {"label": "Road Widening Impact", "type": "number"},
#     "future_development_index": {"label": "Future Development Index", "type": "number"},

#     # -------- Ranking --------
#     "similarity_score": {"label": "Similarity Score", "type": "number"},
#     "overall_score": {"label": "Overall Score", "type": "number"},
#     "rank": {"label": "Rank", "type": "number"},
# }


# ATTRIBUTE_GROUPS = {
#     "identity": [
#         "project_name",
#         "location_name",
#         "micromarket",
#         "city_name",
#         "developer_name",
#         "property_type",
#         "bhk_type",
#         "unit_area_sqft",
#         "possession_status",
#     ],

#     "investment": [
#         "price_per_sqft",
#         "rental_yield_percent",
#         "capital_appreciation_rate",
#         "price_growth_yoy",
#         "absorption_rate",
#         "demand_index",
#         "investment_score",
#     ],

#     "livability": [
#         "amenities_score",
#         "safety_score",
#         "walkability_score",
#         "green_area_score",
#         "density_score",
#         "lifestyle_score",
#     ],

#     "connectivity": [
#         "distance_to_it_hub",
#         "distance_to_metro",
#         "distance_to_highway",
#         "travel_time_cbd_min",
#         "connectivity_score",
#     ],

#     "social_infrastructure": [
#         "distance_to_school",
#         "distance_to_hospital",
#         "distance_to_mall",
#         "social_infra_score",
#     ],

#     "developer_quality": [
#         "developer_rating",
#         "project_completion_rate",
#         "delay_history_score",
#         "construction_quality_score",
#         "brand_value_score",
#     ],

#     "project_configuration": [
#         "total_units",
#         "units_available",
#         "floor_count",
#         "parking_ratio",
#         "unit_mix_score",
#     ],

#     "legal_compliance": [
#         "rera_status",
#         "approval_status",
#         "land_title_clearance",
#         "compliance_score",
#     ],

#     "financials": [
#         "total_cost",
#         "base_price",
#         "additional_charges",
#         "maintenance_cost",
#         "cost_efficiency_score",
#     ],

#     "future_growth": [
#         "upcoming_infra_score",
#         "metro_impact_score",
#         "road_widening_impact",
#         "future_development_index",
#     ],

#     "ranking": [
#         "similarity_score",
#         "overall_score",
#         "rank",
#     ],
# }