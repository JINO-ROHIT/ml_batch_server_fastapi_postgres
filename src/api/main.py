from logging import getLogger

from fastapi import FastAPI
from src.api.routers import routers
from configs.configurations import APIConfigurations

from src.jobs.job import scheduler

logger = getLogger(__name__)


app = FastAPI(
    title=APIConfigurations.title,
    description=APIConfigurations.description,
    version=APIConfigurations.version,
)

app.include_router(routers.router, prefix="", tags=[""])

scheduler.start()