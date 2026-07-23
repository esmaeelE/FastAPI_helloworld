async def test_root(client):
    resp = await client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Hello World"}


async def test_health(client):
    resp = await client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "version" in data


async def test_docs(client):
    resp = await client.get("/docs")
    assert resp.status_code == 200


async def test_scalar(client):
    resp = await client.get("/scalar")
    assert resp.status_code == 200
