import mysql.connector
from tkinter import messagebox
from mysql.connector import Error


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

def gtIdName():
    """Get class labels (id and name) from the database."""
    conn = connect_mysql_db()  # Ensure you are connected to the DB
    if conn is None:
        return {}  # Return an empty dictionary if connection fails
    
    cursor = conn.cursor()
    
    # Query to get all class labels from the database
    cursor.execute("SELECT id, name FROM student")  # Modify the query if necessary
    
    # Fetch all the records
    records = cursor.fetchall()
    
    # Create a dictionary with id as key and label as value
    class_labels = {record[0]: record[1] for record in records}
    
    # Close the connection
    cursor.close()
    conn.close()
    
    return class_labels

def insert_attendance(student_id, class_id):
    try:
        # Connect to the database
        conn = connect_mysql_db()
        if conn.is_connected():
            cursor = conn.cursor()

            # Check if the combination of student_id and class_id already exists
            cursor.execute("SELECT COUNT(*) FROM attendance WHERE student_id = %s AND class_id = %s", 
                           ("{}".format(student_id), "{}".format(class_id)))
            record_exists = cursor.fetchone()[0] > 0

            if record_exists:
                print("Attendance for this student in this class already exists.")
            else:
                # Prepare the SQL query to insert attendance
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



