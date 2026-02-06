def evaluate_project_impact(data: dict):
    green = data.get("green_space_pct", 0)
    transit = data.get("public_transport", 0)
    carbon = data.get("carbon_emissions", 100)
    jobs = data.get("jobs_created", 0)
    business = data.get("local_business_boost", 0)

    env_score = (green * 0.4) + (transit * 0.4) + ((100 - carbon) * 0.2)
    econ_score = (min(jobs / 1000, 1) * 50) + (business * 0.5)
    final_score = (env_score * 0.6) + (econ_score * 0.4)

    if final_score >= 80:
        rating = "Excellent"
    elif final_score >= 60:
        rating = "Good"
    elif final_score >= 40:
        rating = "Moderate"
    else:
        rating = "Poor"

    return {
        "environment_score": round(env_score, 2),
        "economic_score": round(econ_score, 2),
        "development_quality_score": round(final_score, 2),
        "rating": rating
    }
