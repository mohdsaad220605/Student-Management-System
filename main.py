from crud_operation import add_student, update_student, delete_student, print_students, print_student

input_str=""
print("Welcome to Student Management system")


while True:
    print("Enter 1. to Add student")
    print("Enter 2. to Update student")
    print("Enter 3. to Delete student")
    print("Enter 4. to show all students")
    print("Enter 5. to show information of a particular student")
    print("Enter any other key to exit")

    input_str = input("Enter your choice: ")

    if input_str == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        stream = input("Enter student stream: ")
        rollNo = int(input("Enter student roll number: "))
        add_student(name, age, stream, rollNo)

    elif input_str == "2":
        rollNo = int(input("Enter student roll number to update: "))
        new_name = input("Enter new student name: ")
        new_age = int(input("Enter new student age: "))
        new_stream = input("Enter new student stream: ")
        update_student(rollNo, new_name, new_age, new_stream)

    elif input_str == "3":
        rollNo = int(input("Enter student roll number to delete: "))
        delete_student(rollNo)

    elif input_str == "4":
        print_students()

    elif input_str == "5":
        rollNo = int(input("Enter student's roll number: "))
        print_student(rollNo)

    else:
        print("Exiting the program.")
        break
    print("\n-----------------------------\n")

