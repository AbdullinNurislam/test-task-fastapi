from fastapi import FastAPI
import uvicorn

from api.metric import router as metric_router


app = FastAPI(
    title="test task FastAPI",
    description="Service for collecting service performance metrics",
)
app.include_router(metric_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
