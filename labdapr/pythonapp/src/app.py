from flask import Flask
from controllers.orders_controller import OrdersController
from services.order_service import OrderService
from dapr.clients import DaprClient
import sys

app = Flask(__name__)

# Initialize the Dapr client
dapr_client = DaprClient()

# Initialize the OrderService
order_service = OrderService(dapr_client)

# Initialize the OrdersController
orders_controller = OrdersController(order_service)

# Debug statement to print the Python module search paths
print("PYTHONPATH:", sys.path)

@app.route('/orders', methods=['POST'])
def create_order():
    return orders_controller.create_order()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)