import cv2
import face_recognition
from PIL import Image
import os
import sqlite3
from tkinter import messagebox


def connect_db():
    """Connect to the SQLite database."""
    try:
        conn = sqlite3.connect("students.db")  # Use your database path
        return conn
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
        return None


def save_image(image, user_id, base_dir):
    """Save the user's image in a folder specific to their ID."""
    # Create the user-specific folder
    user_folder = os.path.join(base_dir, f"user_{user_id}")
    os.makedirs(user_folder, exist_ok=True)

    # Find the next available number for the file name
    existing_files = os.listdir(user_folder)
    numbers = [int(f.split('.')[0]) for f in existing_files if f.split('.')[0].isdigit()]
    next_number = max(numbers, default=0) + 1

    # Create the file path for saving
    file_path = os.path.join(user_folder, f"{next_number}.jpg")
    
    # Save the image to the specified path
    image.save(file_path)
    return file_path


def save_face(name, student_id):
    """Capture a student's face, encode it, and save the data."""
    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()
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
                # Convert the OpenCV image (BGR) to PIL Image (RGB)
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(image)
                break

        cam.release()
        cv2.destroyAllWindows()

        # Save the image using PIL
        base_dir = r"C:\Users\DISAL\OneDrive\Desktop"  # Update base directory as needed
        image_path = save_image(pil_image, student_id, base_dir)

        # Load and encode the captured face
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            face_encoding = encodings[0].tobytes()

            # Save name, student ID, and encoding in the database
            cursor.execute(
                "INSERT INTO students (id, name, face_encoding) VALUES (?, ?, ?)",
                (student_id, name, face_encoding)
            )
            conn.commit()

            messagebox.showinfo("Success", f"Face data for {name} saved successfully.\nImage saved at {image_path}")
        else:
            messagebox.showerror("Error", "No face detected. Please try again.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        conn.close()


# Example usage
save_face("John Doe", "12345")
