from student_data import students

def add_student(name, age, stream, rollNo):
    for student in students:
        if student['rollNo'] == rollNo:
            print(f"Student with roll number {rollNo} already exists.")
            return
    student = {
        'rollNo': rollNo,
        'name': name,
        'age': age,
        'stream': stream
    }
    students.append(student)
    print(f"Student {name} added successfully.")


def print_students():
    if len(students) == 0:
        print("No students found.")
        return
    for student in students:
        roll_no = student['rollNo']
        name = student['name']
        age = student['age']
        stream = student['stream']
    
        print(f"Roll no: {roll_no}, Name: {name}, Age: {age}, Stream: {stream}")
    print(f"Total students: {len(students)}")

def update_student(rollNo, new_name, new_age, new_stream):
    for student in students:
        if student['rollNo'] == rollNo:
            student['name'] = new_name
            student['age'] = new_age
            student['stream'] = new_stream
            print(f"Student with roll number {rollNo} updated successfully.")
            return
    print(f"Student with roll number {rollNo} not found.")

def delete_student(rollNo):
    for student in students:
        if student['rollNo'] == rollNo:
            students.remove(student)
            print(f"Student with roll number {rollNo} deleted successfully.")
            return
    print(f"Student with roll number {rollNo} not found.")

def print_student(rollNo):
    for student in students:
        if student['rollNo'] == rollNo:
            name = student['name']
            age = student['age']
            stream = student['stream']
            print(f"Roll no: {rollNo}, Name: {name}, Age: {age}, Stream: {stream}")
            return
    print(f"Student with roll number {rollNo} not found.")

