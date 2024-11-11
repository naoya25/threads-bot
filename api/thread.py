from api.threads_client import post_request


def create_text_thread(user_id, text):
    endpoint = f"/{user_id}/threads"
    data = {"text": text, "media_type": "TEXT"}
    response = post_request(endpoint, data)
    return response.get("id")


def publish_thread(user_id, creation_id):
    endpoint = f"/{user_id}/threads_publish"
    data = {"creation_id": creation_id}
    return post_request(endpoint, data)
