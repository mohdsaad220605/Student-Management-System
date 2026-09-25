# Student Management System

## Project Overview

A command-line application for managing student records. Users can add, update, delete, and view students using each student's roll number.

## Features

- Add a student with a name, age, stream, and unique roll number
- Update a student's details by roll number
- Delete a student by roll number
- Display all students and the total number of records
- Look up one student by roll number
- Report duplicate roll numbers and roll numbers that are not found

## Technologies and Tools

- Python 3
- Python standard library; no third-party packages are required
- A terminal or command prompt to run the application

## Install and Run

1. Install Python 3 if it is not already installed. On Windows, verify the installation in PowerShell:

	```powershell
	py --version
	```

	On macOS or Linux, use:

	```bash
	python3 --version
	```

2. Open a terminal in the folder containing `main.py`, `crud_operation.py`, and `student_data.py`.

3. No package installation is needed. Start the application with:

	```powershell
	py main.py
	```

	On macOS or Linux, run:

	```bash
	python3 main.py
	```

4. Choose a menu option and enter the requested student information. Enter any other menu choice to exit.

## Testing

There is no automated test suite included. You can manually check the main operations from the application menu:

1. Choose option `1` and add a student, for example: name `Ava`, age `20`, stream `Science`, roll number `101`.
2. Choose option `4` and confirm the new student appears in the list.
3. Choose option `5`, enter roll number `101`, and confirm the student's details are displayed.
4. Choose option `2`, enter roll number `101`, update one or more details, and confirm the update message appears.
5. Try adding another student with roll number `101` and confirm the duplicate is rejected.
6. Choose option `3`, enter roll number `101`, then choose option `4` to confirm the student was deleted.
7. Try looking up or deleting a roll number that does not exist and confirm the application reports that it was not found.

Student records are kept in memory only and are cleared when the application exits. Restart the program before repeating the checks.
