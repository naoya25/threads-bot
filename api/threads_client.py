import requests
from config.settings import ACCESS_TOKEN, API_BASE_URL


def get_request(endpoint):
    url = f"{API_BASE_URL}{endpoint}"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def post_request(endpoint, data):
    url = f"{API_BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()
