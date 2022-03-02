from fastapi import APIRouter

router = APIRouter()


@router.get("/app")
async def ping_app():
    return {"detail": "app is up"}
