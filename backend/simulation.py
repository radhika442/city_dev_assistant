import random

def run_simulations(data):
    return {
        "best_case": {
            "id": random.randint(1, 10),
            "traffic": random.choice(["Low", "Medium", "High"]),
            "sustainability": random.randint(70, 95)
        },
        "worst_case": {
            "id": random.randint(11, 20),
            "traffic": random.choice(["Low", "Medium", "High"]),
            "sustainability": random.randint(30, 60)
        }
    }
