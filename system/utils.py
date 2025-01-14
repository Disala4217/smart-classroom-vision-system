import os
from tkinter import messagebox
from database import connect_mysql_db

def save_image(image, user_id, base_dir):
    """Save the user's image in a folder specific to their ID."""
    try:
        user_folder = os.path.join(base_dir, f"user_{user_id}")
        os.makedirs(user_folder, exist_ok=True)

        # Find the next available file name
        existing_files = os.listdir(user_folder)
        numbers = [int(f.split('.')[0]) for f in existing_files if f.split('.')[0].isdigit()]
        next_number = max(numbers, default=0) + 1
        file_path = os.path.join(user_folder, f"{next_number}.jpg")

        image.save(file_path)
        return file_path
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save image: {e}")
        return None
def save_student(name, student_id):
    """Save student details into the database."""
    # Get database connection
    mysql_conn = connect_mysql_db()
    if mysql_conn is None:
        return

    try:
        mysql_cursor = mysql_conn.cursor()

        # Parameterized query
        query = "INSERT INTO `student` (`id`, `name`) VALUES (%s, %s)"
        values = (student_id, name)

        # Execute the query
        mysql_cursor.execute(query, values)
        mysql_conn.commit()
        print("Data inserted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if mysql_cursor:
            mysql_cursor.close()
        if mysql_conn:
            mysql_conn.close()

def save_class(subject, grade, teacher_id):
    """Save class details into the database."""
    # Get database connection
    mysql_conn = connect_mysql_db()
    if mysql_conn is None:
        return

    try:
        mysql_cursor = mysql_conn.cursor()

        # Parameterized query to prevent SQL injection
        query = "INSERT INTO `class` (`grade`, `subject`, `datetime`, `teacher_id`) VALUES (%s, %s, NOW(), %s)"
        values = (grade, subject, teacher_id)
        mysql_cursor.execute(query, values)
        mysql_conn.commit()
        print("Class details inserted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if mysql_cursor:
            mysql_cursor.close()
        if mysql_conn:
            mysql_conn.close()


def register_Teacher(name, Teacher_ID):
    """Save teacher details into the database."""
    # Get database connection
    mysql_conn = connect_mysql_db()
    if mysql_conn is None:
        return

    try:
        mysql_cursor = mysql_conn.cursor()

        # Parameterized query
        query = "INSERT INTO `teacher` (`id`, `name`) VALUES (%s, %s)"
        values = (Teacher_ID, name)

        # Execute the query
        mysql_cursor.execute(query, values)
        mysql_conn.commit()
        print("Data inserted successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if mysql_cursor:
            mysql_cursor.close()
        if mysql_conn:
            mysql_conn.close()