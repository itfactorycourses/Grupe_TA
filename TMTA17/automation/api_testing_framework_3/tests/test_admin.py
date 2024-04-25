from requests_folder.request_status import get_status

class TestAdmin:
    def test_api_status(self):
        assert get_status().status_code == 200, f"Invalid status, expected 200, actual, {get_status().status_code}"
        assert get_status().json()["status"] == "OK"
