from loguru import logger
from fastapi import APIRouter, Depends
from typing import List

from src.db.connect import conn
from src.db import crud

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
def predict(data: List[List[float]]):
    crud.create_entry(data)
    return {"success": "data received for prediction!"}

@router.post("/predict_batch")
def predict_batch():
    current = time.time()
    logger.info("Batch job triggered")
    crud.predict_all()
    logger.info(f"Batch Job took {time.time() - current} seconds")
    return {"success": "batch prediction done!"}