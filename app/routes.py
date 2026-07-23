import logging

from fastapi import APIRouter
from pydantic import BaseModel

logger = logging.getLogger(__name__)

router = APIRouter()


class Message(BaseModel):
    message: str


class Health(BaseModel):
    status: str
    version: str


@router.get("/", response_model=Message)
async def root() -> Message:
    logger.info("root endpoint called")
    return Message(message="Hello World")


@router.get("/health", response_model=Health)
async def health() -> Health:
    logger.debug("health check")
    return Health(status="ok", version="1.0.0")
