from api.threads_client import ThreadsClient
from models.media_type import MediaType
from typing import Optional


client = ThreadsClient()


def get_user_id():
    response = client.get("/me")
    return response.get("id")


def create_thread(
    user_id,
    text,
    media_url: Optional[str] = None,
    media_type: Optional[MediaType] = None,
):
    endpoint = f"/{user_id}/threads"
    data = {"text": text, "media_type": "TEXT"}
    if media_url:
        if media_type not in MediaType:
            raise ValueError("無効なメディアタイプです")
        data[f"{media_type.lower}_url"] = media_url
        data["media_type"] = media_type.upper

    return client.post(endpoint, data).get("id")


def publish_thread(user_id, creation_id):
    endpoint = f"/{user_id}/threads_publish"
    data = {"creation_id": creation_id}
    return client.post(endpoint, data).get("id")
