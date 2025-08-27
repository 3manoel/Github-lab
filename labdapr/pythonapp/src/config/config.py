import os

class Config:
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    DAPR_PORT = os.getenv('DAPR_PORT', '3500')
    DAPR_HOST = os.getenv('DAPR_HOST', 'localhost')
    ORDER_SERVICE_URL = os.getenv('ORDER_SERVICE_URL', f'http://{DAPR_HOST}:{DAPR_PORT}/v1.0/invoke/order-service/method/orders')