import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ================= DATABASE =================

con = sqlite3.connect("student.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Student(
    USN TEXT PRIMARY KEY,
    Name TEXT NOT NULL,
    Branch TEXT NOT NULL,
    Phone TEXT NOT NULL
)
""")

con.commit()


# ================= FUNCTIONS =================

def clear_fields():
    usn_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)


def refresh_students():
    for item in tree.get_children():
        tree.delete(item)

    cur.execute("SELECT * FROM Student")
    students = cur.fetchall()

    for student in students:
        tree.insert("", tk.END, values=student)


def add_student():

    usn = usn_entry.get().strip()
    name = name_entry.get().strip()
    branch = branch_entry.get().strip()
    phone = phone_entry.get().strip()

    if usn == "" or name == "" or branch == "" or phone == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    try:
        cur.execute(
            "INSERT INTO Student VALUES (?, ?, ?, ?)",
            (usn, name, branch, phone)
        )

        con.commit()

        messagebox.showinfo(
            "Success",
            "Student Added Successfully"
        )

        clear_fields()
        refresh_students()

    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Error",
            "USN Already Exists"
        )


def search_student():

    usn = usn_entry.get().strip()

    if usn == "":
        messagebox.showwarning(
            "Warning",
            "Enter USN to search"
        )
        return

    cur.execute(
        "SELECT * FROM Student WHERE USN=?",
        (usn,)
    )

    student = cur.fetchone()

    if student:

        name_entry.delete(0, tk.END)
        branch_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)

        name_entry.insert(0, student[1])
        branch_entry.insert(0, student[2])
        phone_entry.insert(0, student[3])

    else:
        messagebox.showerror(
            "Not Found",
            "Student Not Found"
        )


def update_student():

    usn = usn_entry.get().strip()
    name = name_entry.get().strip()
    branch = branch_entry.get().strip()
    phone = phone_entry.get().strip()

    if usn == "":
        messagebox.showwarning(
            "Warning",
            "Enter USN"
        )
        return

    cur.execute(
        "SELECT * FROM Student WHERE USN=?",
        (usn,)
    )

    student = cur.fetchone()

    if not student:
        messagebox.showerror(
            "Error",
            "Student Not Found"
        )
        return

    if name == "" or branch == "" or phone == "":
        messagebox.showwarning(
            "Warning",
            "Please fill all fields"
        )
        return

    cur.execute("""
        UPDATE Student
        SET Name=?, Branch=?, Phone=?
        WHERE USN=?
    """, (name, branch, phone, usn))

    con.commit()

    messagebox.showinfo(
        "Success",
        "Student Updated Successfully"
    )

    refresh_students()


def delete_student():

    usn = usn_entry.get().strip()

    if usn == "":
        messagebox.showwarning(
            "Warning",
            "Enter USN"
        )
        return

    cur.execute(
        "SELECT * FROM Student WHERE USN=?",
        (usn,)
    )

    student = cur.fetchone()

    if not student:
        messagebox.showerror(
            "Error",
            "Student Not Found"
        )
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this student?"
    )

    if confirm:

        cur.execute(
            "DELETE FROM Student WHERE USN=?",
            (usn,)
        )

        con.commit()

        messagebox.showinfo(
            "Success",
            "Student Deleted Successfully"
        )

        clear_fields()
        refresh_students()


def count_students():

    cur.execute("SELECT COUNT(*) FROM Student")

    count = cur.fetchone()[0]

    messagebox.showinfo(
        "Student Count",
        f"Total Students: {count}"
    )


def show_branch_statistics():

    cur.execute("""
        SELECT Branch, COUNT(*)
        FROM Student
        GROUP BY Branch
    """)

    data = cur.fetchall()

    if not data:
        messagebox.showinfo(
            "Statistics",
            "No Student Records Found"
        )
        return

    result = ""

    for branch, count in data:
        result += f"{branch} : {count} students\n"

    messagebox.showinfo(
        "Branch Statistics",
        result
    )


def sort_students():

    for item in tree.get_children():
        tree.delete(item)

    cur.execute(
        "SELECT * FROM Student ORDER BY Name ASC"
    )

    students = cur.fetchall()

    for student in students:
        tree.insert("", tk.END, values=student)


def close_application():

    con.close()
    root.destroy()


# ================= GUI =================

root = tk.Tk()

root.title("Student Management System V3")
root.geometry("900x600")


# ================= TITLE =================

title = tk.Label(
    root,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold")
)

title.pack(pady=15)


# ================= INPUT FRAME =================

input_frame = tk.Frame(root)

input_frame.pack(pady=10)


tk.Label(
    input_frame,
    text="USN"
).grid(row=0, column=0, padx=10, pady=5)

usn_entry = tk.Entry(input_frame, width=25)

usn_entry.grid(row=0, column=1, padx=10, pady=5)


tk.Label(
    input_frame,
    text="Name"
).grid(row=1, column=0, padx=10, pady=5)

name_entry = tk.Entry(input_frame, width=25)

name_entry.grid(row=1, column=1, padx=10, pady=5)


tk.Label(
    input_frame,
    text="Branch"
).grid(row=2, column=0, padx=10, pady=5)

branch_entry = tk.Entry(input_frame, width=25)

branch_entry.grid(row=2, column=1, padx=10, pady=5)


tk.Label(
    input_frame,
    text="Phone"
).grid(row=3, column=0, padx=10, pady=5)

phone_entry = tk.Entry(input_frame, width=25)

phone_entry.grid(row=3, column=1, padx=10, pady=5)


# ================= BUTTON FRAME =================

button_frame = tk.Frame(root)

button_frame.pack(pady=10)


tk.Button(
    button_frame,
    text="Add Student",
    width=15,
    command=add_student
).grid(row=0, column=0, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Search",
    width=15,
    command=search_student
).grid(row=0, column=1, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Update",
    width=15,
    command=update_student
).grid(row=0, column=2, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Delete",
    width=15,
    command=delete_student
).grid(row=0, column=3, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Clear",
    width=15,
    command=clear_fields
).grid(row=1, column=0, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Refresh",
    width=15,
    command=refresh_students
).grid(row=1, column=1, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Sort by Name",
    width=15,
    command=sort_students
).grid(row=1, column=2, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Student Count",
    width=15,
    command=count_students
).grid(row=1, column=3, padx=5, pady=5)


tk.Button(
    button_frame,
    text="Branch Statistics",
    width=15,
    command=show_branch_statistics
).grid(row=2, column=1, columnspan=2, pady=5)


# ================= TABLE =================

table_frame = tk.Frame(root)

table_frame.pack(fill="both", expand=True, padx=20, pady=10)


columns = ("USN", "Name", "Branch", "Phone")

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)


for column in columns:

    tree.heading(
        column,
        text=column
    )

    tree.column(
        column,
        width=150
    )


tree.pack(
    fill="both",
    expand=True
)


# ================= CLOSE BUTTON =================

tk.Button(
    root,
    text="Exit",
    width=15,
    command=close_application
).pack(pady=10)


# ================= START =================

refresh_students()

root.protocol(
    "WM_DELETE_WINDOW",
    close_application
)

root.mainloop()