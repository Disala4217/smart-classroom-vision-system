import mysql.connector
from mysql.connector import Error
from database import insert_attendance

classID=0
StudentID=0

def setClassID(class_id):
    global classID
    classID=class_id

def setStudent(Student_ID):
    global StudentID
    StudentID=Student_ID
    markAttendence()


def markAttendence():
    insert_attendance(StudentID,classID)
    