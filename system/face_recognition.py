import cv2
from tkinter import messagebox
from PIL import Image
import time
from face_detection import detect_faces
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def save_face(student_id):
    cap = cv2.VideoCapture(0)
    count = 0
    person_dir = os.path.join("DataSet", student_id)
    os.makedirs(person_dir, exist_ok=True)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            filepath = os.path.join(person_dir, f"img{count}.jpg")
            cv2.imwrite(filepath, face)
            count += 1
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("Face Capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 100: 
            break

    cap.release()
    cv2.destroyAllWindows()
    
save_face( 2000)