import pytest
import requests

@pytest.fixture()
def api_address():
    return "http://localhost:8080"

class TestTestResource:

    ENDPOINT = "/test"

    def test_get_endpoint(self, api_address):
        response = requests.get(f"{api_address}{self.ENDPOINT}")

        assert response.status_code == 200
        assert response.json() == {"message": "GET request received"}

    def test_post_endpoint(self, api_address):
        payload = {"key": "value"}
        response = requests.post(f"{api_address}{self.ENDPOINT}", json=payload)

        assert response.status_code == 201
        assert response.json() == {
            "message": "POST request received",
            "data": payload
        }