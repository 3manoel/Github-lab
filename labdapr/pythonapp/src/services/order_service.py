class OrderService:
    def __init__(self, dapr_client):
        self.dapr_client = dapr_client

    def create_order(self, order_data):
        # Logic to create an order
        response = self.dapr_client.invoke_method(
            method_name='createOrder',
            data=order_data
        )
        return response

    def update_order(self, order_id, order_data):
        # Logic to update an existing order
        response = self.dapr_client.invoke_method(
            method_name='updateOrder',
            data={'id': order_id, **order_data}
        )
        return response

    def get_order(self, order_id):
        # Logic to retrieve an order by its ID
        response = self.dapr_client.invoke_method(
            method_name='getOrder',
            data={'id': order_id}
        )
        return response

    def delete_order(self, order_id):
        # Logic to delete an order by its ID
        response = self.dapr_client.invoke_method(
            method_name='deleteOrder',
            data={'id': order_id}
        )
        return response