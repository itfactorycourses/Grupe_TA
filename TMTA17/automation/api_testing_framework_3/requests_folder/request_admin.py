import requests
from faker import Faker
from requests_folder import request_data


def get_status():
    return requests.get(f'{request_data.REQUEST_URL}/status')


def generate_token():
    data_generator = Faker()
    email = data_generator.email()
    json_data = {
        "clientName": "tmta17",
        "clientEmail": email
    }
    response = requests.post(f'{request_data.REQUEST_URL}/api-clients/', json=json_data)
    return response
