from tkinter import *
from tkinter import messagebox
from face_recognition1 import save_face
from utils import save_student
from utils import register_Teacher
from utils import save_class
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from tkinter import Tk, Label, Button
from UseModel import recognize
from tkinter import Tk, Label, Entry, Button, messagebox
from tkinter.ttk import Combobox
from utils import End_class
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
            try:
                save_face(student_id)  
                save_student(name, student_id)  
                messagebox.showinfo("Success", f"Student {name} registered successfully!")
                root.destroy() 
            except Exception as e:
                messagebox.showerror("Error", f"Failed to register student: {e}")

           

    register_button = Button(
        root, text="Register Face", font=("Arial", 12),
        bg="green", fg="white", command=register_face
    )
    register_button.pack(pady=10)

    exit_button = Button(
        root, text="Exit", font=("Arial", 12),
        bg="red", fg="white", command=root.destroy
    )
    exit_button.pack(pady=10)

    root.mainloop()
    

def create_gui_Mark_Attendence_and_Moniter_ClassRoom():
    root = Tk()
    root.title("Add a Class")
    root.geometry("400x450")
    root.resizable(False, False)

    # Title Label
    title = Label(root, text="Add A Class", font=("Arial", 18, "bold"), fg="blue")
    title.pack(pady=20)

    style = Style()
    style.configure("TCombobox", font=("Arial", 12), foreground="blue")

    # Subject Selection
    Subject_label = Label(root, text="Select Subject:", font=("Arial", 12))
    Subject_label.pack(pady=10)
    subjects = ["Mathematics", "Science", "History", "English", "Sinhala", "Information and Communication Technology"]
    Subject_combo = Combobox(root, font=("Arial", 12), values=subjects, state="readonly", style="TCombobox")
    Subject_combo.pack(pady=5)
    Subject_combo.set("Select a subject")

    # Grade Selection
    Grade_label = Label(root, text="Select Grade:", font=("Arial", 12))
    Grade_label.pack(pady=10)
    grades = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    Grades_combo = Combobox(root, font=("Arial", 12), values=grades, state="readonly", style="TCombobox")
    Grades_combo.pack(pady=5)
    Grades_combo.set("Select a grade")

    # Teacher ID Entry
    id_label = Label(root, text="Enter Teacher ID:", font=("Arial", 12))
    id_label.pack(pady=10)
    id_entry = Entry(root, font=("Arial", 12))
    id_entry.pack(pady=5)

    def add_class():
        subject = Subject_combo.get().strip()
        grade = Grades_combo.get().strip()
        ID = id_entry.get().strip()

        if subject == "Select a subject" or grade == "Select a grade" or not ID:
            messagebox.showerror("Error", "Please fill in all fields correctly!")
            return

        save_class(subject, grade, ID)
        show_mark_attendance_button(grade)

    def show_mark_attendance_button(grade):
        """Dynamically add 'Mark Attendance' and 'End Class' buttons."""
        MarkAttendance = Button(
            root, text="Mark Attendance", font=("Arial", 12),
            bg="blue", fg="white", command=lambda: recognize(grade)
        )
        MarkAttendance.pack(pady=10)

        ENDCLASS = Button(
            root, text="End Class", font=("Arial", 12),
            bg="blue", fg="white", command=endClass
        )
        ENDCLASS.pack(pady=10)

    def endClass():
        End_class()  
        root.destroy

    AddClass = Button(
        root, text="Add Class", font=("Arial", 12),
        bg="green", fg="white", command=add_class
    )
    AddClass.pack(pady=10)

    root.mainloop()
    
    

def create_gui():
    style = Style(theme="solar") 
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
