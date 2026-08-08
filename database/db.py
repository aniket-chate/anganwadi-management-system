import os
import mysql.connector
from mysql.connector import Error

from config import Config


def get_db():
    """
    Create and return a MySQL connection.

    Works with:
    - Local MySQL during development
    - Aiven MySQL on Vercel
    """

    try:
        host = Config.DB_HOST

        # Automatically enable SSL for Aiven.
        # This means you don't have to manually change the
        # local configuration when switching environments.
        is_aiven = host and "aivencloud.com" in host.lower()

        connection_config = {
            "host": host,
            "port": int(Config.DB_PORT),
            "user": Config.DB_USER,
            "password": Config.DB_PASSWORD,
            "database": Config.DB_NAME,
            "autocommit": False,
            "connection_timeout": 10,
        }

        if is_aiven:
            connection_config.update({
                "ssl_disabled": False,
                "ssl_verify_cert": False,
                "ssl_verify_identity": False,
            })

        connection = mysql.connector.connect(
            **connection_config
        )

        if connection.is_connected():
            return connection

    except Error as e:
        print(f"[Database Error] {e}")

    except Exception as e:
        print(f"[Unexpected Database Error] {e}")

    return None


def close_db(connection):
    """
    Safely close a database connection.
    """

    if connection:
        try:
            if connection.is_connected():
                connection.close()
        except Exception:
            pass