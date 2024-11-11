from services.user_service import fetch_user_id
from services.thread_service import post_text_thread, publish_text_thread

def post_text(text="Hello World!"):
    user_id = fetch_user_id()
    print("ユーザーID:", user_id)
    if not user_id:
        return

    creation_id = post_text_thread(user_id, text)
    print("スレッドの作成に成功しました:", creation_id)
    if not creation_id:
        return

    publish_response = publish_text_thread(user_id, creation_id)
    if publish_response:
        print("スレッドの公開に成功しました:", publish_response)

if __name__ == "__main__":
    post_text("Sample Post Text")
