from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_tasks_route_requires_authentication():
    response = client.get("/tasks/")
    assert response.status_code in (401, 403)
