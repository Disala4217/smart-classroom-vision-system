from tkinter import *
from tkinter import messagebox
from face_recognition import save_face
from utils import save_student
from utils import register_Teacher
from utils import save_class
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from tkinter import Tk, Label, Button


def create_gui_addStudent():
    root = Tk()
    root.title("Add Student")
    root.geometry("400x350")
    root.resizable(False, False)

    # Title Label
    title = Label(root, text="Add Student", font=("Arial", 18, "bold"), fg="blue")
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
            save_face(student_id)
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
    
def create_gui_addTeacher():
    root = Tk()
    root.title("Add Teacher")
    root.geometry("400x350")
    root.resizable(False, False)

    # Title Label
    title = Label(root, text="Add Teacher", font=("Arial", 18, "bold"), fg="blue")
    title.pack(pady=20)

    # Entry for Name
    name_label = Label(root, text="Enter Name:", font=("Arial", 12))
    name_label.pack(pady=10)
    name_entry = Entry(root, font=("Arial", 12))
    name_entry.pack(pady=5)

    # Entry for StudetEACHERnt ID
    id_label = Label(root, text="Enter Teacher ID:", font=("Arial", 12))
    id_label.pack(pady=10)
    id_entry = Entry(root, font=("Arial", 12))
    id_entry.pack(pady=5)

    # Buttons
    def register_TeacherbTN():
        name = name_entry.get().strip()
        Teacher_id = id_entry.get().strip()
        if not name or not Teacher_id:
            messagebox.showerror("Error", "Name and Teacher ID cannot be empty!")
        else:
            register_Teacher(name,Teacher_id)

    register_button = Button(
        root, text="Register Teacher", font=("Arial", 12),
        bg="green", fg="white", command=register_TeacherbTN
    )
    register_button.pack(pady=10)

    exit_button = Button(
        root, text="Exit", font=("Arial", 12),
        bg="red", fg="white", command=root.quit
    )
    exit_button.pack(pady=10)

    root.mainloop()

def create_gui_Mark_Attendence_and_Moniter_ClassRoom():
    root = Tk()
    root.title("Add a Class")
    root.geometry("400x450")
    root.resizable(False, False)

    # Title Label
    title = Label(root, text="Add A class", font=("Arial", 18, "bold"), fg="blue")
    title.pack(pady=20)

    # Entry for Subject
    Subject_label = Label(root, text="Enter Subject:", font=("Arial", 12))
    Subject_label.pack(pady=10)
    Subject_entry = Entry(root, font=("Arial", 12))
    Subject_entry.pack(pady=5)

    # Entry for Grade
    Grade_label = Label(root, text="Enter Grade:", font=("Arial", 12))
    Grade_label.pack(pady=10)
    Grade_entry = Entry(root, font=("Arial", 12))
    Grade_entry.pack(pady=5)

    # Entry for TeacherID
    id_label = Label(root, text="Enter Teacher ID:", font=("Arial", 12))
    id_label.pack(pady=10)
    id_entry = Entry(root, font=("Arial", 12))
    id_entry.pack(pady=5)

    # Buttons
    def add_class():
        subject = Subject_entry.get().strip()
        grade=Grade_entry.get().strip()
        ID=id_entry.get().strip()
        if not subject or not grade or not ID:
            messagebox.showerror("Error", "subject and grade , Teacher ID cannot be empty!")
        else:
            save_class(subject, grade,ID)
            show_mark_attendance_button()
    def show_mark_attendance_button():
        """Dynamically add the 'Mark Attendance' button."""
        MarkAttendance = Button(
            root, text="Mark Attendance", font=("Arial", 12),
            bg="blue", fg="white", command=lambda: messagebox.showinfo("Info", "Mark Attendance clicked!")
        )
        MarkAttendance.pack(pady=10)

    AddClass = Button(
        root, text="Add Class", font=("Arial", 12),
        bg="green", fg="white", command=add_class
    )
    AddClass.pack(pady=10)

    root.mainloop()
    
    

def create_gui():
    style = Style(theme="solar")  #cyborg,solar,darkly.
    root = style.master
    root.title("Smart ClassRoom Vision System")
    root.geometry("400x350")
    root.resizable(False, False)

    # Title Label
    title = Label(
        root, text="Smart ClassRoom Vision System",
        font=("Helvetica", 18, "bold"), fg="#00d1b2", bg="#222"
    )
    title.pack(pady=20)

    # Add Student Button
    add_student_button = Button(
        root, text="Add Student", command=create_gui_addStudent,
        font=("Helvetica", 12), bg="#6c757d", fg="white",
        activebackground="#4caf50", activeforeground="white",
        relief="flat", padx=10, pady=5,width=20,height=1
    )
    add_student_button.pack(pady=10)

    # Add Teacher Button
    add_teacher_button = Button(
        root, text="Add Teacher", command=create_gui_addTeacher,
        font=("Helvetica", 12), bg="#6c757d", fg="white",
        activebackground="#4caf50", activeforeground="white",
        relief="flat", padx=10, pady=5,width=20,height=1
    )
    add_teacher_button.pack(pady=10)

    # Mark Attendance And Moniter ClassRoom
    Mark_Attendace_And_Moniter_bClassRoom_Button = Button(
        root, text="Mark Attendance And\n Moniter ClassRoom", command=create_gui_Mark_Attendence_and_Moniter_ClassRoom,
        font=("Helvetica", 12), bg="#6c757d", fg="white",
        activebackground="#4caf50", activeforeground="white",
        relief="flat", padx=10, pady=5,width=20,height=1
    )
    Mark_Attendace_And_Moniter_bClassRoom_Button.pack(pady=10)

    # Exit Button
    exit_button = Button(
        root, text="Exit", command=root.quit,
        font=("Helvetica", 12), bg="#dc3545", fg="white",
        activebackground="#ff6666", activeforeground="white",
        relief="flat", padx=10, pady=5,width=20,height=1
    )
    exit_button.pack(pady=10)

    root.mainloop()
