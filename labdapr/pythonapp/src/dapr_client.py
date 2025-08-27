def send_order_to_dapr(order):
    import requests
    import json

    dapr_url = "http://localhost:3500/v1.0/invoke/your-dapr-service/method/sendOrder"

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(dapr_url, headers=headers, data=json.dumps(order))

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to send order to Dapr service: {response.status_code} - {response.text}")