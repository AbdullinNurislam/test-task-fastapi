from sqlalchemy import select
from sqlalchemy.sql import func
from sqlalchemy.ext.asyncio import AsyncSession

from models import Metric, Service
from schemas.metric import Metrics


class MetricService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_metric(self, metric_data: Metrics):
        service = await self.session.execute(
            select(Service).where(
                Service.service_name == metric_data.service_name,
                Service.path == metric_data.path,
            )
        )
        service = service.scalar()

        if service is None:
            new_service = Service(
                service_name=metric_data.service_name, path=metric_data.path
            )
            self.session.add(new_service)
            await self.session.commit()
            service = new_service

        new_metric = Metric(
            response_time_ms=metric_data.responseTimeMs, service_id=service.id
        )
        self.session.add(new_metric)
        await self.session.commit()
        return new_metric

    async def get_metrics(self, service_name: str):
        metrics = (
            select(
                Service.path,
                func.min(Metric.response_time_ms).label("min"),
                func.max(Metric.response_time_ms).label("max"),
                func.avg(Metric.response_time_ms).label("average"),
                func.percentile_cont(0.99)
                .within_group(Metric.response_time_ms)
                .label("p99"),
            )
            .select_from(Metric)
            .join(Service, Metric.service_id == Service.id)
            .filter(Service.service_name == service_name)
            .group_by(Service.path)
            .order_by(Service.path)
        )
        result = await self.session.execute(metrics)
        result = result.all()

        return result
