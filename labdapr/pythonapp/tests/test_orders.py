import unittest
from src.controllers.orders_controller import OrdersController
from src.services.order_service import OrderService

class TestOrdersController(unittest.TestCase):

    def setUp(self):
        self.order_service = OrderService()
        self.controller = OrdersController(self.order_service)

    def test_create_order(self):
        order_data = {"item": "Test Item", "quantity": 2}
        response = self.controller.create_order(order_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("order_id", response.json)

    def test_get_order(self):
        order_id = "12345"
        response = self.controller.get_order(order_id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["order_id"], order_id)

    def test_update_order(self):
        order_id = "12345"
        updated_data = {"item": "Updated Item", "quantity": 3}
        response = self.controller.update_order(order_id, updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["item"], "Updated Item")

    def test_delete_order(self):
        order_id = "12345"
        response = self.controller.delete_order(order_id)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()