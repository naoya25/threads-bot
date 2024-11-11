from api.thread import get_user_id, create_thread, publish_thread
from api.media import upload_media
from models.media_type import MediaType
from typing import Optional
import time


def post_thread(
    text: str,
    media_path: Optional[str] = None,
    media_type: Optional[MediaType] = None,
) -> Optional[str]:
    user_id = get_user_id()
    if not user_id:
        return None
    print(f"User ID: {user_id}")

    print(f"Text: {text}")

    media_url = None
    if media_path:
        if media_type not in MediaType:
            raise ValueError("無効なメディアタイプです")

        media_url = upload_media(media_path, media_type)
        if not media_url:
            return None
        print(f"Media URL: {media_url}")
        time.sleep(10)

    thread_id = (
        create_thread(user_id, text, media_url, media_type)
        if media_url
        else create_thread(user_id, text)
    )
    if not thread_id:
        raise Exception("スレッドの作成に失敗しました")
    print(f"Thread ID: {thread_id}")

    time.sleep(10)

    response = publish_thread(user_id, thread_id)
    print(f"Finished: {response}")
    return response
