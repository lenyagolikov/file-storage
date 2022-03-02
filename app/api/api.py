from fastapi import APIRouter

from app.api.handlers import ping

api_router = APIRouter()

api_router.include_router(ping.router, prefix="/ping", tags=["ping"])
