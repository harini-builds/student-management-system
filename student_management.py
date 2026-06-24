import sqlite3

con = sqlite3.connect("student.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Student(
    USN TEXT PRIMARY KEY,
    Name TEXT,
    Branch TEXT,
    Phone TEXT
)
""")

con.commit()

while True:

    print("""
    ===== STUDENT MANAGEMENT SYSTEM V2.1 =====

    1. Add Student
    2. Display Students
    3. Search Student by USN
    4. Search Student by Name
    5. Delete Student
    6. Update Student
    7. Count Students
    8. Display Students by Branch
    9. Exit
    """)

    try:
        ch = int(input("Enter Choice: "))
    except:
        print("Please Enter a Valid Number")
        continue

    # ADD STUDENT
    if ch == 1:

        usn = input("Enter USN: ")
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        phone = input("Enter Phone: ")

        try:

            cur.execute(
                "INSERT INTO Student VALUES(?,?,?,?)",
                (usn, name, branch, phone)
            )

            con.commit()

            print("Student Added Successfully")

        except:
            print("USN Already Exists")

    # DISPLAY STUDENTS
    elif ch == 2:

        cur.execute("SELECT * FROM Student")

        data = cur.fetchall()

        if len(data) == 0:

            print("No Records Found")

        else:

            print("\n===== STUDENT RECORDS =====\n")

            for i in data:

                print("----------------------------")
                print("USN    :", i[0])
                print("Name   :", i[1])
                print("Branch :", i[2])
                print("Phone  :", i[3])
                print("----------------------------")

    # SEARCH BY USN
    elif ch == 3:

        search_usn = input("Enter USN: ")

        cur.execute(
            "SELECT * FROM Student WHERE USN=?",
            (search_usn,)
        )

        data = cur.fetchone()

        if data:

            print("\nStudent Found\n")
            print("USN    :", data[0])
            print("Name   :", data[1])
            print("Branch :", data[2])
            print("Phone  :", data[3])

        else:

            print("Student Not Found")

    # SEARCH BY NAME
    elif ch == 4:

        name = input("Enter Name: ")

        cur.execute(
            "SELECT * FROM Student WHERE Name=?",
            (name,)
        )

        data = cur.fetchall()

        if len(data) == 0:

            print("Student Not Found")

        else:

            for i in data:

                print("----------------------------")
                print("USN    :", i[0])
                print("Name   :", i[1])
                print("Branch :", i[2])
                print("Phone  :", i[3])
                print("----------------------------")

    # DELETE STUDENT
    elif ch == 5:

        del_usn = input("Enter USN to Delete: ")

        cur.execute(
            "DELETE FROM Student WHERE USN=?",
            (del_usn,)
        )

        con.commit()

        if cur.rowcount > 0:

            print("Record Deleted Successfully")

        else:

            print("Student Not Found")

    # UPDATE STUDENT
    elif ch == 6:

        update_usn = input("Enter USN: ")

        cur.execute(
            "SELECT * FROM Student WHERE USN=?",
            (update_usn,)
        )

        data = cur.fetchone()

        if data:

            print("""
            1. Update Name
            2. Update Branch
            3. Update Phone
            """)

            try:
                choice = int(input("Enter Choice: "))
            except:
                print("Invalid Choice")
                continue

            if choice == 1:

                new_name = input("Enter New Name: ")

                cur.execute(
                    "UPDATE Student SET Name=? WHERE USN=?",
                    (new_name, update_usn)
                )

            elif choice == 2:

                new_branch = input("Enter New Branch: ")

                cur.execute(
                    "UPDATE Student SET Branch=? WHERE USN=?",
                    (new_branch, update_usn)
                )

            elif choice == 3:

                new_phone = input("Enter New Phone: ")

                cur.execute(
                    "UPDATE Student SET Phone=? WHERE USN=?",
                    (new_phone, update_usn)
                )

            else:

                print("Invalid Choice")
                continue

            con.commit()

            print("Record Updated Successfully")

        else:

            print("Student Not Found")

    # COUNT STUDENTS
    elif ch == 7:

        cur.execute("SELECT COUNT(*) FROM Student")

        count = cur.fetchone()[0]

        print("Total Students =", count)

    # DISPLAY BY BRANCH
    elif ch == 8:

        branch = input("Enter Branch: ")

        cur.execute(
            "SELECT * FROM Student WHERE Branch=?",
            (branch,)
        )

        data = cur.fetchall()

        if len(data) == 0:

            print("No Students Found")

        else:

            for i in data:

                print("----------------------------")
                print("USN    :", i[0])
                print("Name   :", i[1])
                print("Branch :", i[2])
                print("Phone  :", i[3])
                print("----------------------------")

    # EXIT
    elif ch == 9:

        print("Thank You")
        break

    else:

        print("Invalid Choice")

con.close()