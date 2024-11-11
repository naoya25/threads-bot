import cloudinary
import cloudinary.uploader
import os
import ulid
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True,
)

def upload_media(image_path):
    upload_result = cloudinary.uploader.upload(
        image_path, public_id=f"threads/{ulid.new()}"
    )
    return upload_result["secure_url"]