import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Application Configuration"""

    # Flask Configuration
    SECRET_KEY = os.getenv("SECRET_KEY", "anganwadi-secret-key")

    # Database Configuration
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "AnganwadiDB")

    # Reports Folder
    REPORT_FOLDER = os.path.join(os.getcwd(), "reports")

    # Upload Folder (Future Use)
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")

    # Maximum Upload Size (16 MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # Debug
    DEBUG = os.getenv("FLASK_DEBUG", "True") == "True"