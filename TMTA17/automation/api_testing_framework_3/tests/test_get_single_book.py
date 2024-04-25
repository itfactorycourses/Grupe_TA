from requests_folder.request_get_books import get_single_book


class TestGetSingleBooks:

       def test_get_single_book_by_valid_id(self):
           response = get_single_book(6)
           list_books = [response.json()]
           assert response.json()["id"] == 6, f"Error, invalid id, expected 6, actual {response.json()["id"]}"
           assert response.status_code == 200, f"Error, invalid status code, expected 200, actual {response.status_code}"
           assert len(list_books) == 1, f"Error, invalid number of books returned. Expected 1, actual {len(list_books)}"

       def test_get_single_book_by_invalid_id_float(self):
           response = get_single_book(6.5)
           assert response.status_code == 404, f"Error, invalid id, expected 404, actual {response.status_code}"
           assert response.json()["error"] == "No book with id 6.5"

       def test_get_single_book_by_invalid_id_negative(self):
           response = get_single_book(-6)
           assert response.status_code == 404, f"Error, invalid id, expected 404, actual {response.status_code}"
           assert response.json()["error"] == "No book with id -6", f"Invalid error. Expected: No book with id -6, Actual: {response.json()['error']}"

       def test_get_single_book_by_invalid_id_string(self):
           response = get_single_book('fcernfuiregnr')
           assert response.status_code == 404, f"Error, invalid id, expected 404, actual {response.status_code}"
           assert response.json()["error"] == "No book with id fcernfuiregnr",f"Invalid error. Expected: No book with id fcernfuiregnr, Actual: {response.json()['error']}"