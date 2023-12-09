import uvicorn
# from typing import Union

from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from models import Service, Metric
from core.database import get_session

from api.metric import router as metric_router


app = FastAPI(
    title='test task FastAPI',
    description='Service for collecting service performance metrics'
)

app.include_router(metric_router)


@app.get("/all_services")
async def all_services(
    session: AsyncSession = Depends(get_session),
):
    service = select(Service)
    sess_execute = session.execute(service)
    result = await sess_execute
    result = result.scalars().all()
    return result


@app.get("/all_metrics")
async def all_metrics(
    session: AsyncSession = Depends(get_session),
):
    service = select(Metric)
    sess_execute = session.execute(service)
    result = await sess_execute
    result = result.scalars().all()
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
