import requests
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
API_BASE_URL = "https://graph.threads.net/v1.0"


def get_user_id():
    """認証済みユーザーのIDを取得します。"""
    url = f"{API_BASE_URL}/me"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json().get("id")
    print(f"ユーザーIDの取得に失敗しました: {response.status_code} {response.text}")
    return None


def upload_image(user_id, image_path):
    """画像をアップロードして、メディアIDを取得します。"""
    url = f"{API_BASE_URL}/{user_id}/media"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    files = {"file": open(image_path, "rb")}
    data = {"media_type": "IMAGE"}

    response = requests.post(url, headers=headers, files=files, data=data)
    if response.ok:
        return response.json().get("id")
    print(f"画像のアップロードに失敗しました: {response.status_code} {response.text}")
    return None


def create_thread(user_id, text, media_id=None):
    """指定したテキストと画像（オプション）でスレッドを作成します。"""
    url = f"{API_BASE_URL}/{user_id}/threads"
    data = {"text": text, "media_type": "TEXT"}
    if media_id:
        data["media_id"] = media_id  # 画像メディアIDを追加

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=data, headers=headers)
    if response.ok:
        return response.json().get("id")
    print(f"スレッドの作成に失敗しました: {response.status_code} {response.text}")
    return None


def publish_thread(user_id, creation_id):
    """指定した作成IDを使用してスレッドを公開します。"""
    url = f"{API_BASE_URL}/{user_id}/threads_publish"
    data = {"creation_id": creation_id}
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=data, headers=headers)
    if response.ok:
        return response.json()
    print(f"スレッドの公開に失敗しました: {response.status_code} {response.text}")
    return None


def main():
    """画像とテキストでスレッドの作成と公開を行います。"""
    user_id = get_user_id()
    if not user_id:
        return

    # 投稿テキスト
    text_content = "so cute!"

    # 画像のパス
    image_path = "erika.jpg"
    media_id = upload_image(user_id, image_path)
    if not media_id:
        return

    # 画像付きスレッドの作成
    creation_id = create_thread(user_id, text_content, media_id)
    if not creation_id:
        return

    # スレッドの公開
    publish_response = publish_thread(user_id, creation_id)
    if publish_response:
        print("スレッドの公開に成功しました:", publish_response)


if __name__ == "__main__":
    main()
