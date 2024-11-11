import requests
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
API_BASE_URL = "https://graph.threads.net/v1.0"


class ThreadsClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.headers = {
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }

    def get(self, endpoint):
        response = requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
        )
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=self.headers,
        )
        response.raise_for_status()
        return response.json()
