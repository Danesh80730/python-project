import mysql.connector
from tkinter import *
from tkinter import messagebox
from tabulate import tabulate  # Import tabulate

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="Ganesh",
    password="Ganu@1202",
    database="student_db"
)

# Cursor to execute queries
cursor = db.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    rollno INT PRIMARY KEY,
    name VARCHAR(255),
    marks1 INT,
    marks2 INT
)
""")


# Student Class with MySQL integration
class Student:

    def __init__(self, name='', rollno=0, m1=0, m2=0):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2

    # Function to insert a new student into the database
    def accept(self, Name, Rollno, marks1, marks2):
        query = "INSERT INTO students (rollno, name, marks1, marks2) VALUES (%s, %s, %s, %s)"
        values = (Rollno, Name, marks1, marks2)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success", "Student details added successfully!")

    # Function to display student details from the database
    def display_all(self):
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()
        if records:
            headers = ["RollNo", "Name", "Marks1", "Marks2"]
            table = tabulate(records, headers, tablefmt="grid")
            return table
        else:
            messagebox.showinfo("Info", "No student records found!")
            return None

    # Function to search for a student by rollno
    def search(self, rn):
        query = "SELECT * FROM students WHERE rollno = %s"
        cursor.execute(query, (rn,))
        record = cursor.fetchone()
        if record:
            return record
        else:
            messagebox.showinfo("Info", f"Student with RollNo {rn} not found!")
            return None

    # Function to delete a student by rollno
    def delete(self, rn):
        query = "DELETE FROM students WHERE rollno = %s"
        cursor.execute(query, (rn,))
        db.commit()
        messagebox.showinfo("Success", f"Student with RollNo {rn} deleted successfully!")

    # Function to update a student's rollno
    def update(self, rn, new_roll):
        query = "UPDATE students SET rollno = %s WHERE rollno = %s"
        cursor.execute(query, (new_roll, rn))
        db.commit()
        messagebox.showinfo("Success", f"Student RollNo updated to {new_roll} successfully!")


# Tkinter GUI
class StudentManagementSystem:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("600x500")  # Set window size

        self.name = StringVar()
        self.rollno = IntVar()
        self.marks1 = IntVar()
        self.marks2 = IntVar()
        self.new_rollno = IntVar()

        # Student object
        self.obj = Student()

        # Labels and Entry widgets with padding, alignment, and longer entry fields
        Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10, sticky=E)
        Entry(root, textvariable=self.name, width=30).grid(row=0, column=1, padx=10, pady=10, sticky=W)

        Label(root, text="RollNo").grid(row=1, column=0, padx=10, pady=10, sticky=E)
        Entry(root, textvariable=self.rollno, width=30).grid(row=1, column=1, padx=10, pady=10, sticky=W)

        Label(root, text="Marks1").grid(row=2, column=0, padx=10, pady=10, sticky=E)
        Entry(root, textvariable=self.marks1, width=30).grid(row=2, column=1, padx=10, pady=10, sticky=W)

        Label(root, text="Marks2").grid(row=3, column=0, padx=10, pady=10, sticky=E)
        Entry(root, textvariable=self.marks2, width=30).grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Buttons with padding
        Button(root, text="Add Student", command=self.add_student).grid(row=4, column=0, padx=10, pady=10, sticky=E)
        Button(root, text="Display All", command=self.display_students).grid(row=4, column=1, padx=10, pady=10, sticky=W)

        Button(root, text="Search", command=self.search_student).grid(row=5, column=0, padx=10, pady=10, sticky=E)
        Button(root, text="Delete", command=self.delete_student).grid(row=5, column=1, padx=10, pady=10, sticky=W)

        Button(root, text="Update RollNo", command=self.update_student).grid(row=6, column=0, padx=10, pady=10, sticky=E)
        Entry(root, textvariable=self.new_rollno, width=30).grid(row=6, column=1, padx=10, pady=10, sticky=W)

        # Text box to display the student records in table format
        self.display_area = Text(root, height=10, width=70)
        self.display_area.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def add_student(self):
        self.obj.accept(self.name.get(), self.rollno.get(), self.marks1.get(), self.marks2.get())

    def display_students(self):
        table = self.obj.display_all()
        if table:
            self.display_area.delete(1.0, END)  # Clear previous output
            self.display_area.insert(END, table)  # Display the table

    def search_student(self):
        result = self.obj.search(self.rollno.get())
        if result:
            messagebox.showinfo("Student Found", f"Name: {result[1]}, RollNo: {result[0]}, Marks1: {result[2]}, Marks2: {result[3]}")

    def delete_student(self):
        self.obj.delete(self.rollno.get())

    def update_student(self):
        self.obj.update(self.rollno.get(), self.new_rollno.get())


# Main window
if __name__ == '__main__':
    root = Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
