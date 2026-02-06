def analyze_demographics(data: dict):
    population = data.get("population", 0)

    growth_rate = 0.012  # 1.2% annual growth
    projected_population = int(population * (1 + growth_rate))

    housing_needed = int(projected_population * 0.03)
    workforce = int(projected_population * 0.55)

    return {
        "current_population": population,
        "projected_population": projected_population,
        "housing_units_needed": housing_needed,
        "estimated_workforce": workforce
    }
