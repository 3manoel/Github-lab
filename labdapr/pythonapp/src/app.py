from flask import Flask
from src.controllers.orders_controller import OrdersController

app = Flask(__name__)

# Initialize the OrdersController
orders_controller = OrdersController()

@app.route('/orders', methods=['POST'])
def create_order():
    return orders_controller.create_order()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)