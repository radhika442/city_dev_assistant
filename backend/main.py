from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import CityInput
from traffic import simulate_traffic
from sustainability import evaluate_project_impact
from simulation import run_simulations

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "City Development Assistant Running"}

@app.post("/analyze")
def analyze_city(data: CityInput):
    payload = data.dict()
    return {
        "traffic": simulate_traffic(payload),
        "sustainability": evaluate_project_impact(payload),
        "scenarios": run_simulations(payload)
    }
