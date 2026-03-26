import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Arpita@2005",
        database="order_db"
    )
