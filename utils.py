import os
from tkinter import messagebox
from database import connect_mysql_db
from attendence import setClassID
from attendence import getClassID
import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
classID=0 
def save_student(name, student_id):
    """Save student details into the database."""
    mysql_conn = connect_mysql_db()
    if mysql_conn is None:
        return
    try:
        mysql_cursor = mysql_conn.cursor()
        query = "INSERT INTO `student` (`name`, `id`) VALUES (%s, %s)"
        values = (name,student_id)
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
    global classID
    """Save class details into the database."""
    mysql_conn = connect_mysql_db()
    if mysql_conn is None:
        return
    try:
        mysql_cursor = mysql_conn.cursor()
        query = "INSERT INTO `class` (`grade`, `subject`, `datetime`, `teacher_id`) VALUES (%s, %s, NOW(), %s)"
        values = (grade, subject, teacher_id)
        mysql_cursor.execute(query, values)
        mysql_conn.commit()
        print("Class details inserted successfully.")
        classID=mysql_cursor.lastrowid
        setClassID(classID)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if mysql_cursor:
            mysql_cursor.close()
        if mysql_conn:
            mysql_conn.close()
def End_class():
    classID=getClassID
    """Save class details into the database and mark the class as finished."""
    if not classID:
        print("Error: Invalid classID. Cannot end the class.")
        return
    mysql_conn = connect_mysql_db()
    if mysql_conn is None:
        print("Error: Unable to connect to the database.")
        return
    try:
        mysql_cursor = mysql_conn.cursor()
        query = "UPDATE `class` SET `Status` = 'finished' WHERE `Class_id` = %s;"
        values = (classID,)
        mysql_cursor.execute(query, values)
        mysql_conn.commit()
        print(f"Class with ID {classID} ended successfully.")
    except Exception as e:
        print(f"An error occurred while ending the class: {e}")
    finally:
        classID = 0
        if mysql_cursor:
            mysql_cursor.close()
        if mysql_conn:
            mysql_conn.close()
def register_Teacher(name, Teacher_ID):
    """Save teacher details into the database."""
    mysql_conn = connect_mysql_db()
    if mysql_conn is None:
        return
    try:
        mysql_cursor = mysql_conn.cursor()
        query = "INSERT INTO `teacher` (`id`, `name`) VALUES (%s, %s)"
        values = (Teacher_ID, name)
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
    
