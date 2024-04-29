from requests_folder.request_get_books import get_all_books


class TestGetBooks:

    # test functional testing, positive testing
    def test_get_books_filter_by_type_fiction(self):
        books_list = get_all_books("fiction").json()
        books_type_is_correct = True
        for i in range(len(books_list)):
            if books_list[i]["type"] != "fiction":
                books_type_is_correct = False
                break
        assert get_all_books(
            "fiction").status_code == 200, f"Error, invalid status. Expected 200, actual {get_all_books("fiction").status_code}"
        assert books_type_is_correct == True, "Error, at least one books has the wrong type"

    # test functional testing, positive testing, equivalence partitioning,
    def test_get_books_filter_by_limit(self):
        numer_of_books_returned = len(get_all_books(limit=3).json())
        assert numer_of_books_returned == 3, f"Error, expected three books, returned {numer_of_books_returned}"

    # test functional testing, negative testing, bva
    def test_get_books_filter_by_limit_under_inferior_boundary(self):
        numer_of_books_returned = len(get_all_books(limit=0).json())
        assert numer_of_books_returned == 0, f"Error, expected 0 books, returned {numer_of_books_returned}"
