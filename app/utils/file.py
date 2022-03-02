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

    filehash = md5.hexdigest()

    os.makedirs(os.path.join(SOURCE, await get_short_hash(filehash)))
    os.replace(path, await get_file_path(filehash))

    return filehash


async def get_short_hash(filehash: str) -> str:
    return filehash[:2]


async def get_file_path(filehash: str) -> str:
    dir = await get_short_hash(filehash)
    return os.path.join(SOURCE, dir, filehash)


async def file_exist(path: str) -> bool:
    if os.path.exists(path):
        return True
    return False


async def remove_file(path: str):
    os.remove(path)
