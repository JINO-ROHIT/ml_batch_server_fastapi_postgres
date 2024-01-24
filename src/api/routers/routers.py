from loguru import logger
from fastapi import APIRouter, Depends
from typing import List

from src.db.connect import conn
from src.db.crud import create_entry, retrieve_all, predict_all, remove_all

import time

router = APIRouter()


@router.get("/")
def welcome():
    return {"hello": "there"}

@router.get("/health")
def health():
    print('treiggered')
    return {"health": "ok"}

@router.post("/predict")
async def predict(data: List[List[float]]):
    create_entry(data)
    return {"success": "data received for prediction!"}

@router.post("/predict_batch")
def predict_batch():
    current = time.time()
    logger.info("Batch job triggered")
    predict_all()
    logger.info(f"Batch Job took {time.time() - current} seconds")
    return {"success": "batch prediction done!"}