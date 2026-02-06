import random

def generate_roads(data):
    population = data.get("population", 500000)

    if population < 500_000:
        major = 2
    elif population < 1_500_000:
        major = 4
    else:
        major = 6

    zones = ["CBD", "Residential", "Industrial"]
    roads = []

    for zone in zones:
        for i in range(1, major + 1):
            roads.append(f"{zone}-Corridor-{i}")

    return roads


def simulate_traffic(data):
    roads = generate_roads(data)
    public_transport = data.get("public_transport", 50)
    peak = data.get("peak_hour", True)

    road_stats = {}

    for road in roads:
        base_traffic = random.randint(500, 3000)
        if peak:
            base_traffic *= 1.3

        adjusted = base_traffic * (1 - public_transport / 150)

        congestion = (
            "Low" if adjusted < 700 else
            "Medium" if adjusted < 1500 else
            "High"
        )

        road_stats[road] = {
            "vehicle_count": int(adjusted),
            "avg_speed_kmph": random.randint(15, 55),
            "congestion_level": congestion,
            "lanes": random.choice([2, 4, 6]),
            "signal_time_sec": random.choice([60, 90, 120]),
            "accident_risk": round(min(adjusted / 3000, 1), 2),
            "emergency_priority_lane": random.choice([True, False])
        }

    return {
        "peak_hour": peak,
        "total_roads": len(roads),
        "roads": road_stats
    }
