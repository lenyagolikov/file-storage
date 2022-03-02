import os

import uvicorn
from fastapi import FastAPI

from app.api.api import api_router

app = FastAPI()
app.include_router(api_router)


def main():
    uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT")))


if __name__ == "__main__":
    main()
