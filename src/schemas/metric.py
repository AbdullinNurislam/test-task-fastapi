from pydantic import BaseModel
from datetime import datetime


class Metrics(BaseModel):
    service_name: str
    path: str
    responseTimeMs: float


class MetricsResponse(BaseModel):
    status: str


class ServicesResponse(BaseModel):
    service_name: str
    path: str
    min: float
    max: float
    average: float
    p99: float

    class Config:
        from_attributes = True
