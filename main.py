from services.thread_service import post_thread


def post_text(text="Hello World!"):
    return post_thread(text)


def post_text_with_image(text="Hello World!", image_path=None):
    return post_thread(text, media_path=image_path, media_type="IMAGE")


def post_text_with_video(text="Hello World!", video_path=None):
    return post_thread(text, media_path=video_path, media_type="VIDEO")


if __name__ == "__main__":
    post_text("Sample Post Text")
