import requests
from requests_folder import request_data
from tests import testing_data
from tests.testing_data import token


def submit_order(bookId="", customerName=""):
    json_data = {
        "bookId": bookId,
        "customerName": customerName
    }

    header_data = {'Authorization': token}

    response = requests.post(f'{request_data.REQUEST_URL}/orders', json=json_data, headers=header_data)
    return response


def delete_order(orderId):
    header = {'Authorization': testing_data.token}
    response = requests.delete(f'{request_data.REQUEST_URL}/orders/{orderId}', headers=header)
    return response
