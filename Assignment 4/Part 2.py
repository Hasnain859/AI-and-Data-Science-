# List to store student records
#part 2
students = []

def add_student():
    roll_no = input("Enter Roll Number: ")
    # Prevent duplicate roll numbers
    for student in students:
        if student['roll_no'] == roll_no:
            print("Roll number already exists. Use a unique one.")
            return
    name = input("Enter Name: ")
    subject = input("Enter Subject: ")
    try:
        marks = float(input("Enter Marks: "))
    except ValueError:
        print("Invalid marks. Must be a number.")
        return

    student = {
        "roll_no": roll_no,
        "name": name,
        "subject": subject,
        "marks": marks
    }
    students.append(student)
    print(" Student added successfully.")

def display_students():
    if not students:
        print(" No student records to display.")
        return
    print("\n--- All Student Records ---")
    for s in students:
        print(f"Roll No: {s['roll_no']}")
        print(f"Name: {s['name']}")
        print(f"Subject: {s['subject']}")
        print(f"Marks: {s['marks']}")
    print("---------------------------")

def search_student():
    roll_no = input("Enter Roll Number to search: ")
    for s in students:
        if s["roll_no"] == roll_no:
            print(f" Student Found: Roll No: {s['roll_no']}")
            print(f"Name: {s['name']}")
            print(f"Subject: {s['subject']}")
            print(f"Marks: {s['marks']}")
            return
    print("Student not found.")

def update_marks():
    roll_no = input("Enter Roll Number to update marks: ")
    for s in students:
        if s["roll_no"] == roll_no:
            try:
                new_marks = float(input("Enter new marks: "))
                s["marks"] = new_marks
                print(" Marks updated successfully.")
                return
            except ValueError:
                print(" Invalid input. Marks must be a number.")
                return
    print(" Student not found.")

def delete_student():
    roll_no = input("Enter Roll Number to delete: ")
    for i, s in enumerate(students):
        if s["roll_no"] == roll_no:
            del students[i]
            print(" Student record deleted.")
            return
    print("Student not found.")

def sort_records():
    if not students:
        print(" No student records to sort.")
        return
    students.sort(key=lambda s: s["marks"], reverse=True)
    print("Records sorted by marks (descending).")

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
            print(" Exiting SRMS. Goodbye!")
            break
        else:
            print(" Invalid choice. Please select a valid option (1-7).")

# Run the menu
menu()
