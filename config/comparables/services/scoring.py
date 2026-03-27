# def score_rows(rows: list, comparison_mode: str) -> list:
#     scored = []

#     for row in rows:
#         score = 0.0

#         if comparison_mode == "investment":
#             rate = row.get("rate_sqft", 0) or 0
#             yield_value = row.get("rental_yield", 0) or 0
#             score = (yield_value * 100) + max(0, 20 - (rate / 1000))

#         elif comparison_mode == "living_quality":
#             safety = row.get("safety_score", 0) or 0
#             amenities = 9 if row.get("amenities_score") == "9/10" else 8
#             distance = row.get("distance_to_it_hub", 10) or 10
#             score = safety + amenities + max(0, 10 - distance)

#         else:
#             score = 50

#         row["similarity_score"] = round(score / 30, 2) if comparison_mode == "living_quality" else round(score / 20, 2)
#         scored.append(row)

#     scored.sort(key=lambda x: x.get("similarity_score", 0), reverse=True)
#     return scored

def _safe_number(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def score_rows(rows: list, comparison_mode: str) -> list:
    scored = []

    for index, row in enumerate(rows, start=1):
        score = 0.0

        if comparison_mode == "investment":
            rate = _safe_number(row.get("price_per_sqft") or row.get("avg_rate_sqft"), 0)
            yield_value = _safe_number(row.get("rental_yield_percent"), 0)
            growth = _safe_number(row.get("price_growth_yoy"), 0)
            score = (yield_value * 100) + (growth * 50) + max(0, 20 - (rate / 1000))

        elif comparison_mode == "living_quality":
            safety = _safe_number(row.get("safety_score"), 0)
            amenities = _safe_number(row.get("amenities_score"), 0)
            connectivity = _safe_number(row.get("connectivity_score"), 0)
            score = safety + amenities + connectivity

        elif comparison_mode == "connectivity":
            metro = _safe_number(row.get("distance_to_metro"), 10)
            highway = _safe_number(row.get("distance_to_highway"), 10)
            cbd_time = _safe_number(row.get("travel_time_cbd_min"), 60)
            score = max(0, 10 - metro) + max(0, 10 - highway) + max(0, 60 - cbd_time) / 6

        elif comparison_mode == "developer_quality":
            rating = _safe_number(row.get("developer_rating"), 0)
            completion = _safe_number(row.get("project_completion_rate"), 0) * 10
            quality = _safe_number(row.get("construction_quality_score"), 0)
            score = rating + completion + quality

        elif comparison_mode == "pricing":
            rate = _safe_number(row.get("price_per_sqft") or row.get("avg_rate_sqft"), 0)
            growth = _safe_number(row.get("price_growth_yoy"), 0)
            efficiency = _safe_number(row.get("cost_efficiency_score"), 0)
            score = max(0, 25 - (rate / 1000)) + (growth * 50) + efficiency

        elif comparison_mode == "supply_demand":
            demand = _safe_number(row.get("demand_index"), 0)
            heat = _safe_number(row.get("market_heat_score"), 0)
            ratio = _safe_number(row.get("demand_supply_ratio"), 0)
            score = demand + heat + (ratio * 5)

        else:
            base = _safe_number(row.get("investment_score"), 0)
            live = _safe_number(row.get("livability_score"), 0)
            conn = _safe_number(row.get("connectivity_score"), 0)
            score = max(base, 6.0) + max(live, 6.0) + max(conn, 6.0)

        row["overall_score"] = round(score, 2)
        row["similarity_score"] = round(score / 3, 2)
        row["rank"] = index
        scored.append(row)

    scored.sort(key=lambda x: x.get("overall_score", 0), reverse=True)
    for rank, row in enumerate(scored, start=1):
        row["rank"] = rank
    return scored
