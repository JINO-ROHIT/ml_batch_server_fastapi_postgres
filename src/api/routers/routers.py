from logging import getLogger
from fastapi import APIRouter, Depends

logger = getLogger(__name__)
router = APIRouter()


@router.get("/")
def health():
    return {"hello": "there"}

@router.get("/health")
def health():
    return {"health": "ok"}