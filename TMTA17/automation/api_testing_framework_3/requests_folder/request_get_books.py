import requests
from requests_folder import request_data


def get_all_books(type="", limit=""):
    if type == "" and limit == "":
        return requests.get(f"{request_data.REQUEST_URL}/books")
    if type == "" and limit != "":
        return requests.get(f"{request_data.REQUEST_URL}/books?limit={limit}")
    if type != "" and limit == "":
        return requests.get(f"{request_data.REQUEST_URL}/books?type={type}")
    if type != "" and limit != "":
        return requests.get(f"{request_data.REQUEST_URL}/books?type={type}&limit={limit}")


def get_single_book(book_id):
    return requests.get(f"{request_data.REQUEST_URL}/books/{book_id}")
