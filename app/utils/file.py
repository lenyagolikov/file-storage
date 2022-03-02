import os
import hashlib

import aiofiles
from fastapi import UploadFile

BUF_SIZE = 65536
SOURCE = "store"


async def write_and_hashing_file(file: UploadFile) -> str:
    md5 = hashlib.md5()
    path = os.path.join(SOURCE, file.filename)

    async with aiofiles.open(path, "wb") as f:
        while True:
            data = await file.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            await f.write(data)

    hash = md5.hexdigest()

    os.makedirs(os.path.join(SOURCE, await get_short_hash(hash)), exist_ok=True)
    os.replace(path, await get_file_path(hash))

    return hash


async def get_short_hash(hash: str) -> str:
    return hash[:2]


async def get_file_path(hash: str) -> str:
    dir = await get_short_hash(hash)
    return os.path.join(SOURCE, dir, hash)


async def is_file_exist(path: str) -> bool:
    if os.path.exists(path):
        return True
    return False


async def remove_file(path: str):
    """Удаляет файл. Если директория пустая - удаляет еще и директорию"""
    os.remove(path)

    dirname = os.path.dirname(path)

    if not os.listdir(dirname):
        os.rmdir(dirname)
