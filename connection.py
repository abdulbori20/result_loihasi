import mysql.connector

from database_main import DATABASE_NAME


def get_connection():
    mysql.connector.connect(
        host='localhost',
        user='root',
        password='Abdulboriy',
        database=DATABASE_NAME
    )