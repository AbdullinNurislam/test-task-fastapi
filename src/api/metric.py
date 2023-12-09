from fastapi import APIRouter, Depends
from typing import List
from schemas.metric import Metrics, MetricsResponse, ServicesResponse
from services.metric_service import MetricService
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_session

router = APIRouter(prefix="/metrics")

@router.post("/", response_model=MetricsResponse)
async def add_metric(metric_data: Metrics, session: AsyncSession = Depends(get_session)):
    metric_service = MetricService(session)
    new_metric = await metric_service.add_metric(metric_data)
    return {"status": "ok"}

@router.get("/{service_name}", response_model=List[ServicesResponse])
async def get_metrics(service_name: str, session: AsyncSession = Depends(get_session)):
    metric_service = MetricService(session)
    return await metric_service.get_metrics(service_name)
