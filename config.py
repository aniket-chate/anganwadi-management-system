import os

from dotenv import load_dotenv


load_dotenv()


class Config:

    # ==========================================
    # Flask
    # ==========================================

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "anganwadi-secret-key"
    )


    # ==========================================
    # Database
    # ==========================================

    DB_HOST = os.getenv(
        "DB_HOST",
        "localhost"
    )

    DB_PORT = os.getenv(
        "DB_PORT",
        "3306"
    )

    DB_USER = os.getenv(
        "DB_USER",
        "root"
    )

    DB_PASSWORD = os.getenv(
        "DB_PASSWORD",
        ""
    )

    DB_NAME = os.getenv(
        "DB_NAME",
        "AnganwadiDB"
    )


    # ==========================================
    # Application
    # ==========================================

    REPORT_FOLDER = os.path.join(
        os.getcwd(),
        "reports"
    )

    UPLOAD_FOLDER = os.path.join(
        os.getcwd(),
        "uploads"
    )

    MAX_CONTENT_LENGTH = (
        16 * 1024 * 1024
    )


    # ==========================================
    # Debug
    # ==========================================

    DEBUG = (
        os.getenv(
            "FLASK_DEBUG",
            "False"
        ).lower() == "true"
    )