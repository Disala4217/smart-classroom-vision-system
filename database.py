import mysql.connector
from tkinter import messagebox
from mysql.connector import Error
from distraction import engagement
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
def gtIdName(Grade):
    """Get class labels (id and name) from the database."""
    conn = connect_mysql_db() 
    if conn is None:
        return {} 
    try:
        cursor = conn.cursor() 
        query = "SELECT id, name FROM student WHERE grade = %s;"
        cursor.execute(query, (Grade,))
        records = cursor.fetchall()
        class_labels = {record[0]: record[1] for record in records}
    except Exception as e:
        print(f"An error occurred: {e}")
        class_labels = {}  
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return class_labels
def insert_attendance(student_id, class_id):
    try:
        conn = connect_mysql_db()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM attendance WHERE student_id = %s AND class_id = %s", 
                           ("{}".format(student_id), "{}".format(class_id)))
            record_exists = cursor.fetchone()[0] > 0
            if record_exists:
                deduction_points=engagement()
                print(deduction_points)
                sql_query = """
                UPDATE attendance set engagement_level=engagement_level-%s WHERE student_id=%s AND class_id=%s
                """
                values = ("{}".format(deduction_points),"{}".format(student_id), "{}".format(class_id))
                cursor.execute(sql_query, values)
                conn.commit()
            else:
                sql_query = """
                    INSERT INTO attendance (student_id, class_id, attendance, engagement_level)
                    VALUES (%s, %s, %s, %s)
                """
                values = ("{}".format(student_id), "{}".format(class_id), "1", "100")
                cursor.execute(sql_query, values)
                conn.commit()
                print("Attendance record inserted successfully.")
    except Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()



