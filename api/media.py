from models.media_type import MediaType
import cloudinary
import cloudinary.uploader
import os
import ulid
from dotenv import load_dotenv
import logging

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True,
)


def upload_media(media_path, media_type: MediaType):
    try:
        upload_result = cloudinary.uploader.upload(
            media_path,
            public_id=f"threads/{ulid.new()}",
            resource_type=media_type.lower,
        )
        return upload_result["secure_url"]
    except Exception as e:
        logging.error(f"Error uploading media: {e}")
        return None
