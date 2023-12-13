from pydantic import BaseModel
from typing import List


class Metrics(BaseModel):
    service_name: str
    path: str
    responseTimeMs: float


class MetricsResponse(BaseModel):
    status: str


class ServiceMetrics(BaseModel):
    path: str
    average: float
    min: float
    max: float
    p99: float

    class Config:
        from_attributes = True


class Pagination(BaseModel):
    page: int
    page_size: int
    pages: int
    total: int


class ServiceMetricsResponse(BaseModel):
    pagination: Pagination
    result: List[ServiceMetrics]

class Message404Response(BaseModel):
    detail: str
