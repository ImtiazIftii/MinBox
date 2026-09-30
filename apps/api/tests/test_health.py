from fastapi.testclient import TestClient

from minbox_api.core.config import settings
from minbox_api.main import app

# Creating a TestClient by wrapping FastAPI app instance

client = TestClient(
    app
)  # tells to test on our app / to send fake requests to fastapi without needing server


def test_health_check_returns_200() -> None:

    # making an in-memory get request
    response = client.get(f"{settings.API_V1_STR}/health")
    # assert that the get request code is 200/healthy
    # assert checks if an expression is true or not
    assert response.status_code == 200

    data = response.json()  # formattin the response into json i believe from fast api?
    assert data["status"] == "healthy"
    assert data["version"] == settings.VERSION
    assert data["environment"] == settings.ENVIRONMENT
