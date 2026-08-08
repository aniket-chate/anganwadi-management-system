import mysql.connector
from mysql.connector import Error

from config import Config


def get_db():
    """
    Create and return a MySQL database connection.
    """

    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            autocommit=False
        )

        if connection.is_connected():
            return connection

    except Error as e:
        print(f"[Database Error] {e}")

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