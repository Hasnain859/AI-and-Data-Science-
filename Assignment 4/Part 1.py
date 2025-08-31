##Write a menu-driven program to create a Student Records Management
##System (SRMS) using List and its methods. Your program must include the
##following features:
##a. Add Student - Take name, roll number, subject and marks as input and
##store them into a list.
##b. Display students - show all stored students records in a readable
##format.
##c. Search Student - Search for a student by roll number and display if
##found.
##d. Update record - Update the marks of student using roll number.
##e. Delete Record - Delete a student record using roll number.
##f. Sort Record - Sorting students records by marks (descending order).
##g. Exit.
students = []

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    subject = input("Enter Subject: ")
    try:
        marks = float(input("Enter Marks: "))
    except ValueError:
        print("Invalid marks. Must be a number.")
        return
    students.append([roll_no, name, subject, marks])
    print(" Student added successfully.")

def display_students():
    if not students:
        print("No student records available.")
        return
    print("\n--- All Student Records ---")
    for s in students:
        print(f"Roll No: {s[0]}")
        print(f"Name: {s[1]}")
        print(f"Subject: {s[2]}")
        print(f"Marks: {s[3]}")
    print("---------------------------")

def search_student():
    roll_no = input("Enter Roll Number to search: ")
    for s in students:
        if s[0] == roll_no:
            print(f" Student Found: Roll No: {s[0]}")
            print(f"Name: {s[1]}")
            print(f"Subject: {s[2]}")
            print(f"Marks: {s[3]}")
            return
    print(" Student not found.")

def update_marks():
    roll_no = input("Enter Roll Number to update marks: ")
    for s in students:
        if s[0] == roll_no:
            try:
                new_marks = float(input("Enter new marks: "))
                s[3] = new_marks
                print(" Marks updated successfully.")
                return
            except ValueError:
                print("Invalid input. Marks must be a number.")
                return
    print(" Student not found.")

def delete_student():
    roll_no = input("Enter Roll Number to delete: ")
    for i, s in enumerate(students):
        if s[0] == roll_no:
            del students[i]
            print(" Student record deleted.")
            return
    print("Student not found.")

def sort_records():
    if not students:
        print(" No student records to sort.")
        return
    students.sort(key=lambda x: x[3], reverse=True)
    print(" Records sorted by marks (descending).")

def menu():
    while True:
        print("""
======= Student Records Management System (SRMS) =======
1. Add Student
2. Display Students
3. Search Student
4. Update Marks
5. Delete Record
6. Sort Records by Marks (Descending)
7. Exit
""")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_marks()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            sort_records()
        elif choice == '7':
            print(" Exiting!")
            break
        else:
            print(" Invalid choice. Please select a valid option (1-7).")

# Run the menu
menu()
