# Student Management System - Project Statement

## Problem Statement

Managing basic student details manually can make it difficult to find, update, and keep records consistent. This project provides a simple command-line application for maintaining student records by roll number. It helps users perform common record operations and alerts them when a roll number is duplicated or cannot be found.

## Scope of the Project

The project is a lightweight, single-user command-line tool. Its scope includes:

- Adding a student with a name, age, stream, and roll number
- Updating a student's details by roll number
- Deleting a student by roll number
- Displaying all student records and the total record count
- Looking up an individual student by roll number
- Reporting duplicate roll numbers and missing records

Records are stored in memory while the program is running and are not saved after it exits. The project does not include a graphical interface, database, user accounts, or multi-user access.

## Target Users

- Students learning Python and practicing functions, lists, dictionaries, and basic CRUD operations
- Teachers or tutors who need a small demonstration tool for student record management
- Individual users who want to manage a few student records during a single program session

## High-Level Features

- Interactive numbered menu
- Create, read, update, and delete student records
- Unique roll-number check when adding a record
- Search and not-found feedback for roll-number-based operations
- In-memory data handling with no external package or database setup