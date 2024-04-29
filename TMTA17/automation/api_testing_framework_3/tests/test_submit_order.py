from requests_folder.request_orders import submit_order
from faker import Faker

import tests.testing_data

class TestSubmitOrder:

    data_generator = Faker()

    def test_submit_order_valid_data(self):
        response = submit_order(5, tests.testing_data.customer_name)
        assert response.status_code == 201, f"Invalid status code. Expected 201, actual {response.status_code}"
        assert response.json()[
                   "created"] == True, f"Created field has wrong value. Expected True, actual: {response.json()['created']}"
        assert len(response.json()[
                       "orderId"]) == 21, f"OrderId size is incorrect. Expected 21, actual {len(response.json()["orderId"])}"


    def test_submit_order_missing_book_id(self):
        customer_name = self.data_generator.name()
        response = submit_order(customerName = customer_name)
        assert response.status_code == 400, f"Invalid status code. Expected 400, actual {response.status_code}"
        assert response.json()['error'] == 'Invalid or missing bookId.', f"Invalid error message. Expected Invalid or missing bookId, actual {response.json()['error']}"

    def test_submit_order_missing_customer_name(self):
        response = submit_order(4)
        assert response.status_code == 400, f"Invalid status code. Expected 400, actual {response.status_code}"
        assert response.json()['error'] == 'Invalid or missing customerName.', f"Invalid error message. Expected Invalid or missing customerName, actual {response.json()['error']}"
