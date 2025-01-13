import cv2
import face_recognition
import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image
import os


# MySQL Database connection
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


# Save face image to local storage
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


def save_face(name, student_id):
    """Capture a student's face, encode it, and save the data in MySQL."""
    mysql_conn = connect_mysql_db()

    if mysql_conn is None:
        return

    mysql_cursor = mysql_conn.cursor()

    try:
        # Open webcam
        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            messagebox.showerror("Camera Error", "Cannot access webcam.")
            return

        messagebox.showinfo("Info", "Press 's' to capture an image.")
        pil_image = None

        while True:
            ret, frame = cam.read()
            if not ret:
                messagebox.showerror("Camera Error", "Failed to capture image.")
                break

            cv2.imshow("Capture Face", frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(image)
                break

        cam.release()
        cv2.destroyAllWindows()

        if pil_image is None:
            return

        # Save image locally
        base_dir = r"D:\COMPUTER SCIENCE\INDIVIDUAL PROJECT\Project\faces"  # Update base directory as needed
        image_path = save_image(pil_image, student_id, base_dir)

        if not image_path:
            return

        # Encode the captured face
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            face_encoding = encodings[0].tobytes()

            # Insert into MySQL
            mysql_cursor.execute(
                "INSERT INTO student (id, name, ) VALUES (%s, %s)",
                (student_id, name, face_encoding)
            )
            mysql_conn.commit()

            messagebox.showinfo(
                "Success",
                f"Face data for {name} saved successfully.\nImage saved at {image_path}."
            )
        else:
            os.remove(image_path)  # Remove invalid image
            messagebox.showerror("Error", "No face detected. Please try again.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        mysql_cursor.close()
        mysql_conn.close()


# GUI
def create_gui():
    root = Tk()
    root.title("Attendance System")
    root.geometry("400x350")
    root.resizable(False, False)

    # Title Label
    title = Label(root, text="Attendance System", font=("Arial", 18, "bold"), fg="blue")
    title.pack(pady=20)

    # Entry for Name
    name_label = Label(root, text="Enter Name:", font=("Arial", 12))
    name_label.pack(pady=10)
    name_entry = Entry(root, font=("Arial", 12))
    name_entry.pack(pady=5)

    # Entry for Student ID
    id_label = Label(root, text="Enter Student ID:", font=("Arial", 12))
    id_label.pack(pady=10)
    id_entry = Entry(root, font=("Arial", 12))
    id_entry.pack(pady=5)

    # Buttons
    def register_face():
        name = name_entry.get().strip()
        student_id = id_entry.get().strip()
        if not name or not student_id:
            messagebox.showerror("Error", "Name and Student ID cannot be empty!")
        else:
            save_face(name, student_id)

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
if __name__ == "__main__":
    create_gui()
