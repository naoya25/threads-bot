from api.threads_client import get_request


def get_user_id():
    response = get_request("/me")
    return response.get("id")
