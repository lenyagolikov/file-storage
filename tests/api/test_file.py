from httpx import AsyncClient

prefix = "file"


async def test_upload_file(async_client: AsyncClient):
    with open("tests/image.jpeg", "rb") as f:
        resp = await async_client.post(f"/{prefix}/upload", files={"file": ("filename", f, "image/jpeg")})
        assert resp.status_code == 200
        assert isinstance(resp.json(), str)


async def test_download_file(async_client: AsyncClient):
    params = {"hash": "54b9aa7b609609549bc8f7db101d5db5"}
    resp = await async_client.get(f"/{prefix}/download", params=params)
    headers = resp.headers
    assert headers["content-type"] == "multipart/form-data"
    assert params["hash"] in headers["content-disposition"]


async def test_delete_file(async_client: AsyncClient):
    params = {"hash": "54b9aa7b609609549bc8f7db101d5db5"}
    resp = await async_client.post(f"/{prefix}/delete", params=params)
    assert resp.json() == {"detail": "file was deleted"}
