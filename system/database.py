import mysql.connector
from tkinter import messagebox


def connect_mysql_db():
    """Connect to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="smart_classroom_vision_system"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to MySQL database: {err}")
        return None
