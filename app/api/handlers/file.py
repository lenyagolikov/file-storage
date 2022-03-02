from fastapi import APIRouter, HTTPException, UploadFile, status
from fastapi.responses import FileResponse

from app import utils

router = APIRouter()


@router.get("/download", response_class=FileResponse)
async def download_file(hash: str):
    path = await utils.get_file_path(hash)

    if not await utils.is_file_exist(path):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="file not found")

    return path


@router.post("/upload")
async def upload_file(file: UploadFile):
    return await utils.write_and_hashing_file(file)


@router.post("/delete")
async def delete_file(hash: str):
    path = await utils.get_file_path(hash)

    if not await utils.is_file_exist(path):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="file not found")

    await utils.remove_file(path)

    return {"detail": "file was deleted"}
