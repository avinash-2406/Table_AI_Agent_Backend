# MASTER_COLUMN_REGISTRY = {
#     "project": {"label": "Project", "type": "text"},
#     "location": {"label": "Location", "type": "text"},
#     "config": {"label": "Config", "type": "text"},
#     "area_sqft": {"label": "Area (sq ft)", "type": "number"},
#     "rate_sqft": {"label": "₹/sq ft", "type": "currency"},
#     "transaction_date": {"label": "Transaction Date", "type": "date"},
#     "rental_yield": {"label": "Rental Yield", "type": "percent"},
#     "amenities_score": {"label": "Amenities Score", "type": "text"},
#     "developer_grade": {"label": "Developer Grade", "type": "text"},
#     "distance_to_it_hub": {"label": "Distance to IT Hub", "type": "number"},
#     "safety_score": {"label": "Safety Score", "type": "number"},
#     "similarity_score": {"label": "Similarity Score", "type": "number"},
# }

# ATTRIBUTE_GROUPS = {
#     "identity": ["project", "location", "config", "area_sqft"],
#     "investment": ["rate_sqft", "transaction_date", "rental_yield"],
#     "livability": ["amenities_score", "safety_score"],
#     "connectivity": ["distance_to_it_hub"],
#     "developer_quality": ["developer_grade"],
#     "ranking": ["similarity_score"],
# }


from collections import OrderedDict
from typing import Dict, List

MASTER_COLUMN_REGISTRY: Dict[str, dict] = {
    # -------- Identity --------
    "project_name": {"label": "Project", "type": "text"},
    "project_id": {"label": "Project ID", "type": "text"},
    "developer_name": {"label": "Developer", "type": "text"},
    "property_type": {"label": "Property Type", "type": "text"},
    "property_subtype": {"label": "Property Subtype", "type": "text"},
    "bhk_type": {"label": "BHK", "type": "text"},
    "unit_number": {"label": "Unit Number", "type": "text"},
    "tower_name": {"label": "Tower", "type": "text"},
    "floor_number": {"label": "Floor No.", "type": "number"},
    "possession_status": {"label": "Possession Status", "type": "text"},
    "project_status": {"label": "Project Status", "type": "text"},

    # -------- Location Context --------
    "location_name": {"label": "Location", "type": "text"},
    "micromarket": {"label": "Micromarket", "type": "text"},
    "submarket": {"label": "Submarket", "type": "text"},
    "city_name": {"label": "City", "type": "text"},
    "state_name": {"label": "State", "type": "text"},
    "pincode": {"label": "Pincode", "type": "text"},
    "latitude": {"label": "Latitude", "type": "number"},
    "longitude": {"label": "Longitude", "type": "number"},
    "distance_from_subject_km": {"label": "Distance From Subject (km)", "type": "number"},

    # -------- Area Metrics --------
    "unit_area_sqft": {"label": "Area (sq ft)", "type": "number"},
    "unit_area_sqm": {"label": "Area (sq m)", "type": "number"},
    "carpet_area_sqft": {"label": "Carpet Area (sq ft)", "type": "number"},
    "carpet_area_sqm": {"label": "Carpet Area (sq m)", "type": "number"},
    "saleable_area_sqft": {"label": "Saleable Area (sq ft)", "type": "number"},
    "builtup_area_sqft": {"label": "Built-up Area (sq ft)", "type": "number"},
    "plot_area_sqm": {"label": "Plot Area (sq m)", "type": "number"},
    "fsi_area_sqm": {"label": "FSI Area (sq m)", "type": "number"},

    # -------- Pricing --------
    "price_per_sqft": {"label": "Price Per Sq Ft", "type": "currency"},
    "avg_rate_sqft": {"label": "Avg Rate Per Sq Ft", "type": "currency"},
    "asking_price": {"label": "Asking Price", "type": "currency"},
    "base_price": {"label": "Base Price", "type": "currency"},
    "final_price": {"label": "Final Price", "type": "currency"},
    "ticket_size": {"label": "Ticket Size", "type": "currency"},
    "transaction_value": {"label": "Transaction Value", "type": "currency"},
    "transaction_date": {"label": "Transaction Date", "type": "date"},
    "price_growth_yoy": {"label": "Price Growth YoY (%)", "type": "percent"},
    "discount_percent": {"label": "Discount (%)", "type": "percent"},

    # -------- Investment --------
    "rental_yield_percent": {"label": "Rental Yield (%)", "type": "percent"},
    "capital_appreciation_rate": {"label": "Capital Appreciation Rate", "type": "percent"},
    "irr_percent": {"label": "IRR (%)", "type": "percent"},
    "payback_period_years": {"label": "Payback (Years)", "type": "number"},
    "investment_score": {"label": "Investment Score", "type": "number"},

    # -------- Livability --------
    "amenities_score": {"label": "Amenities Score", "type": "number"},
    "safety_score": {"label": "Safety Score", "type": "number"},
    "walkability_score": {"label": "Walkability Score", "type": "number"},
    "green_area_score": {"label": "Green Area Score", "type": "number"},
    "density_score": {"label": "Density Score", "type": "number"},
    "lifestyle_score": {"label": "Lifestyle Score", "type": "number"},
    "livability_score": {"label": "Livability Score", "type": "number"},

    # -------- Connectivity --------
    "distance_to_it_hub": {"label": "Distance to IT Hub (km)", "type": "number"},
    "distance_to_metro": {"label": "Distance to Metro (km)", "type": "number"},
    "distance_to_highway": {"label": "Distance to Highway (km)", "type": "number"},
    "distance_to_railway": {"label": "Distance to Railway (km)", "type": "number"},
    "travel_time_cbd_min": {"label": "Travel Time to CBD (min)", "type": "number"},
    "travel_time_it_hub_min": {"label": "Travel Time to IT Hub (min)", "type": "number"},
    "connectivity_score": {"label": "Connectivity Score", "type": "number"},

    # -------- Social Infrastructure --------
    "distance_to_school": {"label": "Distance to School (km)", "type": "number"},
    "distance_to_hospital": {"label": "Distance to Hospital (km)", "type": "number"},
    "distance_to_mall": {"label": "Distance to Mall (km)", "type": "number"},
    "distance_to_airport": {"label": "Distance to Airport (km)", "type": "number"},
    "distance_to_park": {"label": "Distance to Park (km)", "type": "number"},
    "social_infra_score": {"label": "Social Infra Score", "type": "number"},

    # -------- Developer Quality --------
    "developer_rating": {"label": "Developer Rating", "type": "number"},
    "developer_grade": {"label": "Developer Grade", "type": "text"},
    "project_completion_rate": {"label": "Project Completion Rate", "type": "number"},
    "delay_history_score": {"label": "Delay History Score", "type": "number"},
    "construction_quality_score": {"label": "Construction Quality Score", "type": "number"},
    "brand_value_score": {"label": "Brand Value Score", "type": "number"},

    # -------- Project Configuration --------
    "total_units": {"label": "Total Units", "type": "number"},
    "units_available": {"label": "Units Available", "type": "number"},
    "units_sold": {"label": "Units Sold", "type": "number"},
    "unsold_units": {"label": "Unsold Units", "type": "number"},
    "floor_count": {"label": "Floor Count", "type": "number"},
    "parking_ratio": {"label": "Parking Ratio", "type": "number"},
    "parking_count": {"label": "Parking Count", "type": "number"},
    "unit_mix_score": {"label": "Unit Mix Score", "type": "number"},

    # -------- Legal Compliance --------
    "rera_status": {"label": "RERA Status", "type": "text"},
    "rera_number": {"label": "RERA Number", "type": "text"},
    "approval_status": {"label": "Approval Status", "type": "text"},
    "land_title_clearance": {"label": "Land Title Clearance", "type": "text"},
    "compliance_score": {"label": "Compliance Score", "type": "number"},
    "litigation_flag": {"label": "Litigation", "type": "text"},

    # -------- Financials --------
    "total_cost": {"label": "Total Cost", "type": "currency"},
    "additional_charges": {"label": "Additional Charges", "type": "currency"},
    "maintenance_cost": {"label": "Maintenance Cost", "type": "currency"},
    "stamp_duty_cost": {"label": "Stamp Duty", "type": "currency"},
    "registration_cost": {"label": "Registration Cost", "type": "currency"},
    "cost_efficiency_score": {"label": "Cost Efficiency Score", "type": "number"},

    # -------- Future Growth --------
    "upcoming_infra_score": {"label": "Upcoming Infra Score", "type": "number"},
    "metro_impact_score": {"label": "Metro Impact Score", "type": "number"},
    "road_widening_impact": {"label": "Road Widening Impact", "type": "number"},
    "future_development_index": {"label": "Future Development Index", "type": "number"},

    # -------- Market Performance --------
    "absorption_rate": {"label": "Absorption Rate", "type": "number"},
    "velocity_index": {"label": "Sales Velocity", "type": "number"},
    "demand_index": {"label": "Demand Index", "type": "number"},
    "market_heat_score": {"label": "Market Heat Score", "type": "number"},
    "launch_count": {"label": "Launch Count", "type": "number"},
    "inventory_months": {"label": "Inventory Months", "type": "number"},

    # -------- Supply Demand --------
    "supply_score": {"label": "Supply Score", "type": "number"},
    "demand_supply_ratio": {"label": "Demand Supply Ratio", "type": "number"},
    "new_supply_units": {"label": "New Supply Units", "type": "number"},
    "sold_to_launched_ratio": {"label": "Sold/Launched Ratio", "type": "number"},

    # -------- Construction Specs --------
    "furnishing_status": {"label": "Furnishing Status", "type": "text"},
    "facing_direction": {"label": "Facing Direction", "type": "text"},
    "view_type": {"label": "View Type", "type": "text"},
    "age_of_property": {"label": "Age Of Property", "type": "number"},
    "construction_stage": {"label": "Construction Stage", "type": "text"},

    # -------- Ranking --------
    "similarity_score": {"label": "Similarity Score", "type": "number"},
    "overall_score": {"label": "Overall Score", "type": "number"},
    "rank": {"label": "Rank", "type": "number"},
}

ATTRIBUTE_GROUPS: Dict[str, List[str]] = {
    "identity": [
        "project_name", "developer_name", "property_type", "bhk_type",
        "tower_name", "floor_number", "possession_status"
    ],
    "location_context": [
        "location_name", "micromarket", "city_name", "state_name", "pincode",
        "distance_from_subject_km"
    ],
    "area_metrics": [
        "unit_area_sqft", "carpet_area_sqft", "saleable_area_sqft", "builtup_area_sqft"
    ],
    "pricing": [
        "price_per_sqft", "avg_rate_sqft", "asking_price", "final_price",
        "ticket_size", "transaction_date", "price_growth_yoy"
    ],
    "investment": [
        "rental_yield_percent", "capital_appreciation_rate", "irr_percent",
        "payback_period_years", "investment_score"
    ],
    "livability": [
        "amenities_score", "safety_score", "walkability_score",
        "green_area_score", "lifestyle_score", "livability_score"
    ],
    "connectivity": [
        "distance_to_it_hub", "distance_to_metro", "distance_to_highway",
        "travel_time_cbd_min", "travel_time_it_hub_min", "connectivity_score"
    ],
    "social_infrastructure": [
        "distance_to_school", "distance_to_hospital", "distance_to_mall",
        "distance_to_park", "social_infra_score"
    ],
    "developer_quality": [
        "developer_grade", "developer_rating", "project_completion_rate",
        "delay_history_score", "construction_quality_score", "brand_value_score"
    ],
    "project_configuration": [
        "total_units", "units_available", "units_sold", "unsold_units",
        "floor_count", "parking_ratio", "unit_mix_score"
    ],
    "legal_compliance": [
        "rera_status", "rera_number", "approval_status",
        "land_title_clearance", "compliance_score", "litigation_flag"
    ],
    "financials": [
        "base_price", "additional_charges", "maintenance_cost",
        "stamp_duty_cost", "registration_cost", "total_cost", "cost_efficiency_score"
    ],
    "future_growth": [
        "upcoming_infra_score", "metro_impact_score",
        "road_widening_impact", "future_development_index"
    ],
    "market_performance": [
        "absorption_rate", "velocity_index", "demand_index",
        "market_heat_score", "launch_count", "inventory_months"
    ],
    "supply_demand": [
        "new_supply_units", "demand_supply_ratio", "sold_to_launched_ratio", "supply_score"
    ],
    "construction_specs": [
        "furnishing_status", "facing_direction", "view_type",
        "age_of_property", "construction_stage"
    ],
    "ranking": ["similarity_score", "overall_score", "rank"],
}

INTENT_TO_GROUPS: Dict[str, List[str]] = {
    "comparable_search": ["identity", "location_context", "area_metrics", "ranking"],
    "investment_screening": ["identity", "location_context", "pricing", "investment", "ranking"],
    "project_lookup": ["identity", "location_context", "area_metrics", "pricing"],
    "market_analysis": ["location_context", "pricing", "market_performance", "supply_demand", "ranking"],
    "developer_analysis": ["identity", "developer_quality", "legal_compliance", "ranking"],
    "livability_analysis": ["identity", "location_context", "livability", "social_infrastructure", "ranking"],
    "connectivity_analysis": ["identity", "location_context", "connectivity", "future_growth", "ranking"],
    "legal_compliance_check": ["identity", "legal_compliance", "ranking"],
    "configuration_analysis": ["identity", "area_metrics", "project_configuration", "construction_specs", "ranking"],
    "pricing_analysis": ["identity", "location_context", "pricing", "financials", "ranking"],
    "supply_demand_analysis": ["identity", "location_context", "market_performance", "supply_demand", "ranking"],
}

COMPARISON_MODE_TO_GROUPS: Dict[str, List[str]] = {
    "living_quality": ["livability", "social_infrastructure", "connectivity"],
    "investment": ["pricing", "investment", "market_performance"],
    "connectivity": ["connectivity", "future_growth"],
    "developer_quality": ["developer_quality", "legal_compliance"],
    "legal": ["legal_compliance"],
    "configuration": ["area_metrics", "project_configuration", "construction_specs"],
    "pricing": ["pricing", "financials"],
    "supply_demand": ["market_performance", "supply_demand"],
    "market": ["pricing", "market_performance", "supply_demand"],
}

KEYWORD_TO_GROUPS: Dict[str, List[str]] = {
    "amenity": ["livability", "social_infrastructure"],
    "amenities": ["livability", "social_infrastructure"],
    "safety": ["livability"],
    "walkability": ["livability"],
    "metro": ["connectivity", "future_growth"],
    "highway": ["connectivity"],
    "it hub": ["connectivity"],
    "developer": ["developer_quality"],
    "rera": ["legal_compliance"],
    "approval": ["legal_compliance"],
    "legal": ["legal_compliance"],
    "price": ["pricing"],
    "pricing": ["pricing"],
    "rate": ["pricing"],
    "yield": ["investment"],
    "rental": ["investment"],
    "investment": ["investment"],
    "demand": ["market_performance", "supply_demand"],
    "supply": ["market_performance", "supply_demand"],
    "configuration": ["project_configuration", "area_metrics"],
    "floor": ["project_configuration", "construction_specs"],
    "area": ["area_metrics"],
    "carpet": ["area_metrics"],
    "cost": ["financials"],
}


def ordered_unique(items: List[str]) -> List[str]:
    return list(OrderedDict.fromkeys([item for item in items if item]))


def expand_attribute_groups(attribute_groups: List[str], intent: str = "", comparison_mode: str = "", query: str = "") -> List[str]:
    final_groups = list(attribute_groups or [])

    final_groups.extend(INTENT_TO_GROUPS.get(intent or "", []))
    final_groups.extend(COMPARISON_MODE_TO_GROUPS.get(comparison_mode or "", []))

    lowered = (query or "").lower()
    for keyword, groups in KEYWORD_TO_GROUPS.items():
        if keyword in lowered:
            final_groups.extend(groups)

    if final_groups and "identity" not in final_groups:
        final_groups.insert(0, "identity")
    if final_groups and "ranking" not in final_groups:
        final_groups.append("ranking")

    return ordered_unique([group for group in final_groups if group in ATTRIBUTE_GROUPS])


def select_columns(attribute_groups: List[str]) -> List[str]:
    columns: List[str] = []
    for group in attribute_groups:
        columns.extend(ATTRIBUTE_GROUPS.get(group, []))
    return ordered_unique([col for col in columns if col in MASTER_COLUMN_REGISTRY])


def build_schema(selected_columns: List[str]) -> List[dict]:
    schema: List[dict] = []
    for col in selected_columns:
        item = MASTER_COLUMN_REGISTRY[col].copy()
        item["key"] = col
        schema.append(item)
    return schema
