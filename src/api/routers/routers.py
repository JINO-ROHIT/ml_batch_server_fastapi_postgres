from logging import getLogger
from fastapi import APIRouter, Depends
from typing import List

from src.db.connect import conn
from src.db.crud import create_entry, retrieve_all, predict_all

logger = getLogger(__name__)
router = APIRouter()


@router.get("/")
def health():
    return {"hello": "there"}

@router.get("/health")
def health():
    return {"health": "ok"}

@router.post("/predict")
async def predict(data: List[List[float]]):
    create_entry(data)
    return {"success": "data received for prediction!"}

@router.post("/predict_batch")
async def predict_batch():
    predict_all()
    return {"success": "batch prediction done!"}