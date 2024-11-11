from api.thread import create_text_thread, publish_thread


def post_text_thread(user_id, text):
    creation_id = create_text_thread(user_id, text)
    return creation_id


def publish_text_thread(user_id, creation_id):
    return publish_thread(user_id, creation_id)
