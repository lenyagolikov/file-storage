from fastapi import status
from httpx import AsyncClient

prefix = "ping"


async def test_ping_app_up(async_client: AsyncClient):
    resp = await async_client.get(f"/{prefix}/app")
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == {"detail": "app is up"}
