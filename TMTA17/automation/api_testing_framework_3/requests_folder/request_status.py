import requests

from requests_folder import test_data


def get_status():
    return requests.get(f'{test_data.REQUEST_URL}/status')
