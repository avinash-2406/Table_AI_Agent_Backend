def score_rows(rows: list, comparison_mode: str) -> list:
    scored = []

    for row in rows:
        score = 0.0

        if comparison_mode == "investment":
            rate = row.get("rate_sqft", 0) or 0
            yield_value = row.get("rental_yield", 0) or 0
            score = (yield_value * 100) + max(0, 20 - (rate / 1000))

        elif comparison_mode == "living_quality":
            safety = row.get("safety_score", 0) or 0
            amenities = 9 if row.get("amenities_score") == "9/10" else 8
            distance = row.get("distance_to_it_hub", 10) or 10
            score = safety + amenities + max(0, 10 - distance)

        else:
            score = 50

        row["similarity_score"] = round(score / 30, 2) if comparison_mode == "living_quality" else round(score / 20, 2)
        scored.append(row)

    scored.sort(key=lambda x: x.get("similarity_score", 0), reverse=True)
    return scored