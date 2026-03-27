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


from typing import Dict, List


def _safe_number(value, default=0.0):
    try:
        if value is None:
            return default
        return float(value)
    except Exception:
        return default


def _financial_score(row: Dict, target_metric: str) -> float:
    rate = _safe_number(row.get("rate_sqft"))
    rental_yield = _safe_number(row.get("rental_yield"))
    land_cost = _safe_number(row.get("land_cost"))
    construction_cost = _safe_number(row.get("construction_cost"))
    finance_cost = _safe_number(row.get("finance_cost"))
    sales_velocity = _safe_number(row.get("sales_velocity"))
    exit_value = _safe_number(row.get("exit_value"))
    approval_delay = _safe_number(row.get("approval_delay"))
    cash_flow_period = _safe_number(row.get("cash_flow_period"))

    base = 0.0
    base += rental_yield * 100
    base += max(0, 30 - (rate / 1000))
    base += min(sales_velocity, 30) * 0.8
    base += max(0, 12 - approval_delay) * 0.7

    if target_metric == "irr":
        total_cost = land_cost + construction_cost + finance_cost
        if total_cost > 0:
            base += min((exit_value / total_cost) * 10, 25)

        if cash_flow_period > 0:
            base += max(0, 24 - cash_flow_period) * 0.5

    return base


def _living_quality_score(row: Dict) -> float:
    amenities = _safe_number(row.get("amenities_score"))
    safety = _safe_number(row.get("safety_score"))
    distance = _safe_number(row.get("distance_to_it_hub"), 10)
    developer_bonus = 0

    grade = str(row.get("developer_grade", "")).upper()
    if grade == "A+":
        developer_bonus = 3
    elif grade == "A":
        developer_bonus = 2
    elif grade == "B+":
        developer_bonus = 1

    return amenities + safety + max(0, 10 - distance) + developer_bonus


def _pricing_score(row: Dict) -> float:
    rate = _safe_number(row.get("rate_sqft"))
    area = _safe_number(row.get("area_sqft"))

    score = 0.0
    score += max(0, 20 - (rate / 1000))
    score += min(area / 100, 10)
    return score


def score_rows(rows: List[Dict], parsed_query: Dict) -> List[Dict]:
    comparison_mode = parsed_query.get("comparison_mode", "generic")
    target_metric = parsed_query.get("target_metric", "generic")

    scored = []

    for row in rows:
        row = dict(row)

        if comparison_mode in ["financial", "investment"]:
            score = _financial_score(row, target_metric)

        elif comparison_mode == "living_quality":
            score = _living_quality_score(row)

        elif comparison_mode == "pricing":
            score = _pricing_score(row)

        else:
            score = 50.0

        row["similarity_score"] = round(score, 2)
        scored.append(row)

    scored.sort(key=lambda x: x.get("similarity_score", 0), reverse=True)
    return scored