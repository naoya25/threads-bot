import requests
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
API_BASE_URL = "https://graph.threads.net/v1.0"


def get_user_id():
    url = f"{API_BASE_URL}/me"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json().get("id")
    return None


def create_text_thread(user_id, text):
    url = f"{API_BASE_URL}/{user_id}/threads"
    data = {"text": text, "media_type": "TEXT"}

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=data, headers=headers)
    if response.ok:
        return response.json().get("id")
    return None


def publish_thread(user_id, creation_id):
    url = f"{API_BASE_URL}/{user_id}/threads_publish"
    data = {"creation_id": creation_id}
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=data, headers=headers)
    if response.ok:
        return response.json()
    return None


def post_text(text="Hello World!"):
    # ユーザーIDの取得
    user_id = get_user_id()
    print("ユーザーID:", user_id)
    if not user_id:
        return

    # スレッドの作成
    creation_id = create_text_thread(user_id, text)
    print("スレッドの作成に成功しました:", creation_id)
    if not creation_id:
        return

    # スレッドの公開
    publish_response = publish_thread(user_id, creation_id)
    if publish_response:
        print("スレッドの公開に成功しました:", publish_response)


if __name__ == "__main__":
    post_text("Sample Post Text")
