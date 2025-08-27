class OrdersController:
    def __init__(self, order_service):
        self.order_service = order_service

    def create_order(self, order_data):
        # Logic to create an order using the order_service
        return self.order_service.create_order(order_data)

    def get_order(self, order_id):
        # Logic to retrieve an order using the order_service
        return self.order_service.get_order(order_id)

    def update_order(self, order_id, order_data):
        # Logic to update an order using the order_service
        return self.order_service.update_order(order_id, order_data)

    def delete_order(self, order_id):
        # Logic to delete an order using the order_service
        return self.order_service.delete_order(order_id)