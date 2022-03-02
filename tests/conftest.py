import asyncio
import os
from typing import AsyncGenerator, Generator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    loop = asyncio.new_event_loop()
    try:
        yield loop
    finally:
        loop.close()


@pytest.fixture
def app() -> FastAPI:
    from app.main import app
    return app


@pytest.fixture
async def async_client(app: FastAPI) -> AsyncGenerator:
    async with AsyncClient(
        app=app, base_url=f"http://{os.getenv('HOST')}:{os.getenv('PORT')}"
    ) as ac:
        yield ac
