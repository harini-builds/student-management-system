while True:

    print("""
    ===== STUDENT MANAGEMENT SYSTEM =====

    1. Add Student
    2. Display Students
    3. Search Student
    4. Delete Student
    5. Update Student
    6. Count Students
    7. Display Students by Branch
    8. Exit
    """)

    try:
        ch = int(input("Enter your choice: "))
    except:
        print("Please enter a valid number")
        continue

    # ADD STUDENT
    if ch == 1:

        f = open("student.txt", "a")

        n = int(input("How many students? "))

        for i in range(n):

            usn = input("Enter USN: ")
            name = input("Enter Name: ")
            branch = input("Enter Branch: ")
            phone = input("Enter Phone: ")

            f.write(usn + "," + name + "," + branch + "," + phone + "\n")

        f.close()

        print("Student Added Successfully")

    # DISPLAY STUDENTS
    elif ch == 2:

        try:
            f = open("student.txt", "r")

            print("\n===== STUDENT RECORDS =====\n")

            for line in f:
                print(line)

            f.close()

        except:
            print("No Records Found")

    # SEARCH STUDENT
    elif ch == 3:

        search_usn = input("Enter USN to Search: ")

        found = False

        try:

            f = open("student.txt", "r")

            for line in f:

                data = line.strip().split(",")

                if data[0] == search_usn:

                    found = True

                    print("\nStudent Found")
                    print("USN    :", data[0])
                    print("Name   :", data[1])
                    print("Branch :", data[2])
                    print("Phone  :", data[3])

            f.close()

            if found == False:
                print("Student Not Found")

        except:
            print("No Records Found")

    # DELETE STUDENT
    elif ch == 4:

        del_usn = input("Enter USN to Delete: ")

        found = False

        try:

            f = open("student.txt", "r")

            temp = []

            for line in f:

                data = line.strip().split(",")

                if data[0] == del_usn:
                    found = True
                else:
                    temp.append(line)

            f.close()

            f = open("student.txt", "w")

            for record in temp:
                f.write(record)

            f.close()

            if found:
                print("Record Deleted Successfully")
            else:
                print("Student Not Found")

        except:
            print("No Records Found")

    # UPDATE STUDENT
    elif ch == 5:

        update_usn = input("Enter USN to Update: ")

        found = False

        try:

            f = open("student.txt", "r")

            temp = []

            for line in f:

                data = line.strip().split(",")

                if data[0] == update_usn:

                    found = True

                    print("""
                    1. Update Name
                    2. Update Branch
                    3. Update Phone
                    """)

                    choice = int(input("Enter Choice: "))

                    if choice == 1:
                        data[1] = input("Enter New Name: ")

                    elif choice == 2:
                        data[2] = input("Enter New Branch: ")

                    elif choice == 3:
                        data[3] = input("Enter New Phone: ")

                    line = ",".join(data) + "\n"

                temp.append(line)

            f.close()

            f = open("student.txt", "w")

            for record in temp:
                f.write(record)

            f.close()

            if found:
                print("Record Updated Successfully")
            else:
                print("Student Not Found")

        except:
            print("No Records Found")

    # COUNT STUDENTS
    elif ch == 6:

        try:

            f = open("student.txt", "r")

            count = 0

            for line in f:
                count += 1

            f.close()

            print("Total Students =", count)

        except:
            print("No Records Found")

    # DISPLAY STUDENTS BY BRANCH
    elif ch == 7:

        branch = input("Enter Branch: ")

        found = False

        try:

            f = open("student.txt", "r")

            for line in f:

                data = line.strip().split(",")

                if data[2].lower() == branch.lower():

                    found = True

                    print(line)

            f.close()

            if found == False:
                print("No Students Found")

        except:
            print("No Records Found")

    # EXIT
    elif ch == 8:

        print("Thank You")
        break

    else:
        print("Invalid Choice")