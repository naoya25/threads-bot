from services.thread_service import post_thread
from models.media_type import MediaType


def post_text(text="Hello World!"):
    return post_thread(text)


def post_text_with_image(text="Hello World!", image_path=None):
    return post_thread(text, media_path=image_path, media_type=MediaType.IMAGE)


def post_text_with_video(text="Hello World!", video_path=None):
    return post_thread(text, media_path=video_path, media_type=MediaType.VIDEO)


if __name__ == "__main__":
    # post_text("Sample Post Text")
    # post_text_with_image("Sample Post Text with Image", "media/sample.PNG")
    post_text_with_video("Sample Post Text with Video", "media/sample_video.mp4")
