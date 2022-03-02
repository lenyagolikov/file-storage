from fastapi import APIRouter

from app.api.handlers import ping, file

api_router = APIRouter()

api_router.include_router(ping.router, prefix="/ping", tags=["ping"])
api_router.include_router(file.router, prefix="/file", tags=["file"])
