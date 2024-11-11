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


def create_post_with_image_url(user_id, text, image_url):
    url = f"{API_BASE_URL}/{user_id}/threads"
    data = {
        "text": text,
        "image_url": image_url,
        "media_type": "IMAGE",
    }
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=data, headers=headers)
    if response.ok:
        return response.json().get("id")
    else:
        print("エラー:", response.status_code, response.text)
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
    else:
        print("エラー:", response.status_code, response.text)
        return None


def post_text_with_image(text="Hello World!", image_url=None):
    # ユーザーIDの取得
    user_id = get_user_id()
    print("ユーザーID:", user_id)
    if not user_id:
        return

    # スレッドの作成
    creation_id = create_post_with_image_url(user_id, text, image_url)
    print("スレッドの作成に成功しました:", creation_id)
    if not creation_id:
        return

    # スレッドの公開
    publish_response = publish_thread(user_id, creation_id)
    if publish_response:
        print("スレッドの公開に成功しました:", publish_response)


if __name__ == "__main__":
    image_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiThh51O_5PBczGCVOAZqWk0NniNOu2Fxun8BlELAmHwR8Rltl1Gnqb_u0dkHvf34yGijTLvwnjWDAe6f-LtgOXAiX3sj__yCp5rsa2KTeaR0uaGye3zKUaTCUd8PiHDAObRfDSW8JT9qc/s800/hirameki_man.png"
    post_text_with_image("Sample Post with Image URL", image_url)
