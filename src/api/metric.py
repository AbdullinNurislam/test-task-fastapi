from fastapi import APIRouter, Depends, Query, HTTPException
from math import ceil
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from schemas.metric import (
    Metrics,
    MetricsResponse,
    ServiceMetricsResponse,
    Message404Response,
)
from services.metric_service import MetricService


router = APIRouter(prefix="/metrics")


@router.post("/", response_model=MetricsResponse)
async def add_metric(
    metric_data: Metrics, session: AsyncSession = Depends(get_session)
):
    metric_service = MetricService(session)
    await metric_service.add_metric(metric_data)
    return {"status": "ok"}


@router.get(
    "/{service_name}",
    response_model=ServiceMetricsResponse,
    responses={404: {"model": Message404Response}},
)
async def get_metrics(
    service_name: str,
    page: int = Query(1, description="Page number", gt=0),
    page_size: int = Query(10, description="Number of items per page", gt=0, le=100),
    session: AsyncSession = Depends(get_session),
):
    metric_service = MetricService(session)
    metrics = await metric_service.get_metrics(service_name)
    if not metrics:
        raise HTTPException(status_code=404, detail="Metrics not found")

    total = len(metrics)
    pagination = {
        "page": page,
        "page_size": page_size,
        "total": total,
        "pages": ceil(total / page_size) if total else None,
    }

    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    metrics_for_page = metrics[start_idx:end_idx]

    result = [
        {
            "path": metric.path,
            "average": metric.average,
            "min": metric.min,
            "max": metric.max,
            "p99": metric.p99,
        }
        for metric in metrics_for_page
    ]

    return {"pagination": pagination, "result": result}
