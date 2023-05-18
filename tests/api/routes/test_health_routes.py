from starlette.testclient import TestClient

from api.main import init_api


def test_health_endpoint_success():
    """
    Test success response for health endpoint
    """
    client = TestClient(init_api())

    response = client.get("/health")

    assert response.json() == {"status": "Healthy"}
    assert response.status_code == 200
