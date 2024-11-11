from api.thread import get_user_id, create_thread, publish_thread
from api.media import upload_media
from models.media_type import MediaType
from typing import Optional
import time
import logging
from config.logging import setup_logging

setup_logging()


def post_thread(
    text: str,
    media_path: Optional[str] = None,
    media_type: Optional[MediaType] = None,
) -> Optional[str]:
    user_id = get_user_id()
    if not user_id:
        return None
    logging.info(f"User ID: {user_id}")
    logging.info(f"Text: {text}")

    media_url = None
    if media_path:
        if media_type not in MediaType:
            raise ValueError("無効なメディアタイプです")

        media_url = upload_media(media_path, media_type)
        if not media_url:
            return None
        logging.info(f"Media URL: {media_url}")

    thread_id = (
        create_thread(user_id, text, media_url, media_type)
        if media_url
        else create_thread(user_id, text)
    )
    if not thread_id:
        raise Exception("スレッドの作成に失敗しました")
    logging.info(f"Thread ID: {thread_id}")

    if media_type == MediaType.VIDEO:
        time.sleep(30)

    response = publish_thread(user_id, thread_id)
    logging.info(f"Finished: {response}")
    return response
