from api.threads_client import ThreadsClient
from models.media_type import MediaType
from typing import Optional
import logging

client = ThreadsClient()


def get_user_id():
    response = client.get("/me")
    try:
        return response.get("id")
    except Exception as e:
        logging.error(f"Error getting user ID: {e}")
        return None


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

    try:
        return client.post(endpoint, data).get("id")
    except Exception as e:
        logging.error(f"Error creating thread: {e}")
        return None


def publish_thread(user_id, creation_id):
    endpoint = f"/{user_id}/threads_publish"
    data = {"creation_id": creation_id}
    try:
        return client.post(endpoint, data).get("id")
    except Exception as e:
        logging.error(f"Error publishing thread: {e}")
        return None
