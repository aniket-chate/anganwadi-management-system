import mysql.connector
from mysql.connector import Error
from config import Config
import os


def get_db():
    """
    Create and return a MySQL database connection.

    Local development:
        Uses the local MySQL configuration.

    Production/Vercel:
        Uses the Aiven MySQL configuration with SSL/TLS.
    """

    try:
        # Determine whether SSL is required.
        # Set DB_SSL_REQUIRED=true in Vercel for Aiven.
        ssl_required = os.getenv(
            "DB_SSL_REQUIRED", "false"
        ).lower() == "true"

        connection_config = {
            "host": Config.DB_HOST,
            "port": int(os.getenv("DB_PORT", "3306")),
            "user": Config.DB_USER,
            "password": Config.DB_PASSWORD,
            "database": Config.DB_NAME,
            "autocommit": False,
        }

        # Aiven requires an encrypted MySQL connection.
        if ssl_required:
            connection_config.update({
                "ssl_disabled": False,
                "ssl_verify_cert": False,
                "ssl_verify_identity": False,
            })

        connection = mysql.connector.connect(**connection_config)

        if connection.is_connected():
            return connection

    except Error as e:
        print(f"[Database Error] {e}")

    except Exception as e:
        print(f"[Unexpected Database Error] {e}")

    return None


def close_db(connection):
    """
    Safely close the database connection.
    """

    if connection:
        try:
            if connection.is_connected():
                connection.close()
        except Error:
            pass