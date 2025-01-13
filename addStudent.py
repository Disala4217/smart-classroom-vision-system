import cv2
import face_recognition
import mysql.connector
import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Database connection
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="sql203.infinityfree.com",
            user="if0_38095745",
            password="p4ygP0D0yJipq",  # Replace with your actual password
            database="if0_38095745_smart_classroom_vision_system"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to database: {err}")
        return None

# Save face to database
def save_face(name):
    #conn = connect_db()
    #if conn is None:
    #    return

    #cursor = conn.cursor()

    try:
        # Open webcam
        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            messagebox.showerror("Camera Error", "Cannot access webcam.")
            return

        messagebox.showinfo("Info", "Press 's' to capture an image")
        while True:
            ret, frame = cam.read()
            if not ret:
                messagebox.showerror("Camera Error", "Failed to capture image.")
                break

            cv2.imshow("Capture Face", frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite("face.jpg", frame)
                break

        cam.release()
        cv2.destroyAllWindows()

        # Load and encode the captured face
        image = face_recognition.load_image_file("face.jpg")
        encodings = face_recognition.face_encodings(image)

        if encodings:
            face_encoding = encodings[0].tobytes()
            # Save name and encoding in database
            cursor.execute(
                "INSERT INTO students (name, face_encoding) VALUES (%s, %s)",
                (name, face_encoding)
            )
            conn.commit()
            messagebox.showinfo("Success", f"Face data for {name} saved successfully.")
        else:
            messagebox.showerror("Error", "No face detected. Please try again.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        conn.close()

# GUI
def create_gui():
    root = Tk()
    root.title("Attendance System")
    root.geometry("400x300")
    root.resizable(False, False)

    # Title Label
    title = Label(root, text="Attendance System", font=("Arial", 18, "bold"), fg="blue")
    title.pack(pady=20)

    # Entry for Name
    name_label = Label(root, text="Enter Name:", font=("Arial", 12))
    name_label.pack(pady=10)
    name_entry = Entry(root, font=("Arial", 12))
    name_entry.pack(pady=5)

    # Buttons
    def register_face():
        name = name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Name cannot be empty!")
        else:
            save_face(name)

    register_button = Button(
        root, text="Register Face", font=("Arial", 12),
        bg="green", fg="white", command=register_face
    )
    register_button.pack(pady=10)

    exit_button = Button(
        root, text="Exit", font=("Arial", 12),
        bg="red", fg="white", command=root.quit
    )
    exit_button.pack(pady=10)

    root.mainloop()

# Run the GUI
create_gui()
