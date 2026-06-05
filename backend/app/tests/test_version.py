from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_version_endpoint():
    response = client.get("/version")

    assert response.status_code == 200

    payload = response.json()

    assert payload["app"] == "Sentiora AI"
    assert payload["version"] == "0.1.0"