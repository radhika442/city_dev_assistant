from pydantic import BaseModel

class CityInput(BaseModel):
    city_name: str
    population: int
    green_space_pct: int
    public_transport: int
    carbon_emissions: int
    jobs_created: int
    local_business_boost: int
    peak_hour: bool = True
