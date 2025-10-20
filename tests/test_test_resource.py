import pytest
import requests

@pytest.fixture()
def api_address():
    return "http://localhost:8080"

class TestTestResource:
    def test_get_endpoint(self, api_address):
        response = requests.get(f"{api_address}/test")

        assert response.status_code == 200
        assert response.json() == {"message": "GET request received"}