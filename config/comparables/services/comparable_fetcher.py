def fetch_comparables(parsed_query: dict, selected_columns: list) -> list:
    sample = [
        {
            "project": "Project A",
            "location": "Baner",
            "config": "3 BHK",
            "area_sqft": 1400,
            "rate_sqft": 10500,
            "transaction_date": "2024-01-01",
            "rental_yield": 0.03,
            "amenities_score": "9/10",
            "developer_grade": "A",
            "distance_to_it_hub": 3.5,
            "safety_score": 8.8,
        },
        {
            "project": "Project B",
            "location": "Balewadi",
            "config": "3 BHK",
            "area_sqft": 1450,
            "rate_sqft": 10200,
            "transaction_date": "2024-02-01",
            "rental_yield": 0.028,
            "amenities_score": "8/10",
            "developer_grade": "A",
            "distance_to_it_hub": 2.5,
            "safety_score": 8.5,
        },
    ]

    trimmed_rows = []
    for row in sample:
        trimmed = {k: row.get(k) for k in selected_columns if k in row}
        trimmed_rows.append(trimmed)

    return trimmed_rows