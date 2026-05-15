import tkinter as tk
window = tk.Tk()
window.title("Student Management System")
window.geometry("500x650")

def add_student():
    with open ("Dataset.txt","a") as file:
        student_name = e1.get()
        student_rollno = e2.get()
        student_marks = e3.get()
        file.write("\n"+"Name: "+student_name+"  Roll No. : "+student_rollno + " Marks: "+student_marks)
        l2.config(text = "Student Name : "+student_name+" Added Successfully")

def remove_student():
    student_name = e1.get()
    student_rollno = e2.get()
    student_marks = e3.get()
    with open("Dataset.txt", "r") as file:
        data = file.readlines()

    with open("Dataset.txt", "w") as file:
        for line in data:
            if not (student_name in line and student_rollno in line):
                file.write(line)
    l3.config(text="Student "+student_name+" Removed Successfully")

def remove_all_students() :
    with open("Dataset.txt", "w") as file:
        data = ""
        file.write(data)
        l5.config(text = "All Students Removed.")

def search_student():
    new_student = e1.get()
    student_rollno = e2.get()
    student_marks = e3.get()
    with open("Dataset.txt", "r") as file:
        data = file.readlines()

    for line in data:
        if new_student in line and student_rollno in line and student_marks in line:
            l4.config(text="Student Present in dataset")
        else:
            l4.config(text="Student Not Present in dataset")

def view_students():
    with open ("Dataset.txt","r") as file:
        data = file.read()
        l5.config(text = data)

l1 = tk.Label(window, text = "  STUDENT MANAGEMENT SYSTEM  ")
l1.pack(side = "top")
l6 = tk.Label(window, text = "")
l6.pack()
l1 = tk.Label(window, text = " Enter  Name :")
l1.pack()
e1 = tk.Entry(window)
e1.pack()
l1 = tk.Label(window, text = " Enter  Roll No :")
l1.pack()
e2 = tk.Entry(window)
e2.pack()
l1 = tk.Label(window, text = " Enter  Marks :")
l1.pack()
e3 = tk.Entry(window)
e3.pack()
l6 = tk.Label(window, text = "")
l6.pack()
b1 = tk.Button(window, text = " 1. Add   Student " , command = add_student)
b1.pack()
l2 = tk.Label(window, text = "")
l2.pack()
l6 = tk.Label(window, text = "")
l6.pack()
b2 = tk.Button(window, text = "2. Remove Student " , command = remove_student)
b2.pack()
l3 = tk.Label(window, text = "")
l3.pack()
l6 = tk.Label(window, text = "")
l6.pack()
b3 = tk.Button(window, text = "3. Search Student ", command = search_student)
b3.pack()
l4 = tk.Label(window, text = "")
l4.pack()
l6 = tk.Label(window, text = "")
l6.pack()
b4 = tk.Button(window, text = " 4. View all Students " , command = view_students)
b4.pack()
l6 = tk.Label(window, text = "")
l6.pack()
l6 = tk.Label(window, text = "")
l6.pack()
b4 = tk.Button(window, text = "5. Remove all Students " , command = remove_all_students)
b4.pack()
l6 = tk.Label(window, text = "")
l6.pack()
l6 = tk.Label(window, text = "")
l6.pack()
l6 = tk.Label(window, text = "")
l6.pack()
l6 = tk.Label(window, text = "")
l6.pack()
l5 = tk.Label(window, text = "")
l5.pack()
l6 = tk.Label(window, text = "")
l6.pack(side="bottom")

window.mainloop()