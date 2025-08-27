from flask import Flask
from controllers.orders_controller import OrdersController
import sys

app = Flask(__name__)

# Initialize the OrdersController
orders_controller = OrdersController()

# Debug statement to print the Python module search paths
print("PYTHONPATH:", sys.path)

@app.route('/orders', methods=['POST'])
def create_order():
    return orders_controller.create_order()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)