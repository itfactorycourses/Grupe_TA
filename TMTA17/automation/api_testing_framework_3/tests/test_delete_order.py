from requests_folder.request_orders import submit_order, delete_order
import tests.testing_data


class TestDeleteOrder:

    def test_delete_existing_order(self):

        order_id = submit_order(5,tests.testing_data.customer_name).json()["orderId"]
        response = delete_order(order_id)
        assert response.status_code == 204, f"Error, invalid status code. Expected 204, actual {response.status_code}"
