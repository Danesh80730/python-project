# python-project
Student Management System
A simple desktop-based application developed using Python, Tkinter, and MySQL for managing student records. This system allows users to add, view, search, update, and delete student records, with details such as roll number, name, and marks.

Features
Add Student: Insert new student records into the database.
View All Students: Display all students' information in a tabular format.
Search Student: Search for a student by roll number.
Update Roll Number: Modify the roll number of an existing student.
Delete Student: Remove a student from the database.
The student data is stored in a MySQL database, and Tkinter provides a graphical user interface for ease of use. The tabulate library is used to display records in a formatted table.

Requirements
Python 3.x
MySQL Server
Required Python Libraries:
mysql-connector-python
tkinter
tabulate
Installation

git clone https://github.com/yourusername/student-management-system.git
Install the required dependencies:


pip install mysql-connector-python tabulate

Set up the MySQL database:
Create a MySQL database named student_db.
Update the MySQL credentials (host, user, password) in the script according to your setup.

Run the application:
python student_management_system.py

Database Structure
The application uses a MySQL table students to store student details. The table is automatically created if it does not exist.

Table Structure:
Field	Type	Description
rollno	INT (PK)	Student roll number
name	VARCHAR(255)	Student name
marks1	INT	Marks in subject 1
marks2	INT	Marks in subject 2

Usage![WhatsApp Image 2024-09-06 at 2 33 41 PM](https://github.com/user-attachments/assets/0212bf62-4c28-4888-909b-4ee28ed3e005)
![WhatsApp Image 2024-09-06 at 2 33 57 PM](https://github.com/user-attachments/assets/a61bed84-23d6-4cd6-8e91-e462f3ff798b)
![WhatsApp Image 2024-09-06 at 2 34 18 PM](https://github.com/user-attachments/assets/18336c3c-2997-4b30-9a18-d1303f123810)

Adding a Student: Fill in the fields (Name, RollNo, Marks1, Marks2) and click Add Student.
Viewing Students: Click on Display All to view all students in a table format.
Searching for a Student: Enter the RollNo and click Search to find a student.
Updating RollNo: Enter the RollNo to update, the new RollNo, and click Update RollNo.
Deleting a Student: Enter the RollNo and click Delete to remove the student from the database.
