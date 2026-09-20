students = []

def add_student():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    students.append({
        "id": id,
        "name": name,
        "age": age,
        "course": course
    })
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\nID | Name | Age | Course")
    for s in students:
        print(s["id"], "|", s["name"], "|", s["age"], "|", s["course"])


def search_student():
    id = int(input("Enter Student ID: "))

    for s in students:
        if s["id"] == id:
            print("ID:", s["id"])
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Course:", s["course"])
            return

    print("Student not found.")


def delete_student():
    id = int(input("Enter Student ID: "))

    for s in students:
        if s["id"] == id:
            students.remove(s)
            print("Student deleted.")
            return

    print("Student not found.")


while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
