from tkinter import *
from tkinter import messagebox
from face_recognition import save_face
from utils import save_student


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
            save_student(name,student_id)

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
