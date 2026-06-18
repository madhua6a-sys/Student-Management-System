# Student Management System
# Demonstrates: CRUD, Functions, File Handling, Data Management, Business Logic
# Author: Madhu Tiwari

import json
import os

FILE_NAME = "students.json"

# File Setup

def load_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_data(students):
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)

# Grade and Average Calculation

def calculate_grade(marks):
    """Return grade based on average marks."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def calculate_average(marks_list):
    return round(sum(marks_list) / len(marks_list), 2)

# CRUD Operations

# CREATE
def add_student(students):
    print("\n--- Add Student ---")
    roll = input("Enter Roll Number: ").strip()

    if roll in students:
        print("Student with this roll number already exists!")
        return

    name = input("Enter Student Name: ").strip()

    subjects = ["Math", "Science", "English"]
    marks_list = []

    for subject in subjects:
        while True:
            try:
                mark = float(input("Enter marks for " + subject + " (0-100): "))
                if 0 <= mark <= 100:
                    marks_list.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    average = calculate_average(marks_list)
    grade = calculate_grade(average)

    marks_dict = {}
    for i in range(len(subjects)):
        marks_dict[subjects[i]] = marks_list[i]

    students[roll] = {
        "name": name,
        "marks": marks_dict,
        "average": average,
        "grade": grade
    }

    save_data(students)
    print("Student '" + name + "' added successfully! Average: " + str(average) + ", Grade: " + grade)

# READ
def view_all_students(students):
    print("\n--- All Students ---")
    if not students:
        print("No student records found.")
        return

    print("Roll\t\tName\t\t\tAverage\t\tGrade")
    print("-" * 55)
    for roll, data in students.items():
        print(roll + "\t\t" + data["name"] + "\t\t\t" + str(data["average"]) + "\t\t" + data["grade"])

def search_student(students):
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number to search: ").strip()

    if roll not in students:
        print("Student not found.")
        return

    data = students[roll]
    print("\nRoll Number : " + roll)
    print("Name        : " + data["name"])
    print("Marks       :")
    for subject, mark in data["marks"].items():
        print("  " + subject + ": " + str(mark))
    print("Average     : " + str(data["average"]))
    print("Grade       : " + data["grade"])

# UPDATE
def update_student(students):
    print("\n--- Update Student ---")
    roll = input("Enter Roll Number to update: ").strip()

    if roll not in students:
        print("Student not found.")
        return

    print("Updating marks for: " + students[roll]["name"])
    subjects = list(students[roll]["marks"].keys())
    marks_list = []

    for subject in subjects:
        while True:
            try:
                mark = float(input("Enter new marks for " + subject + " (0-100): "))
                if 0 <= mark <= 100:
                    marks_list.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    average = calculate_average(marks_list)
    grade = calculate_grade(average)

    marks_dict = {}
    for i in range(len(subjects)):
        marks_dict[subjects[i]] = marks_list[i]

    students[roll]["marks"] = marks_dict
    students[roll]["average"] = average
    students[roll]["grade"] = grade

    save_data(students)
    print("Record updated! New Average: " + str(average) + ", New Grade: " + grade)

# DELETE
def delete_student(students):
    print("\n--- Delete Student ---")
    roll = input("Enter Roll Number to delete: ").strip()

    if roll not in students:
        print("Student not found.")
        return

    name = students[roll]["name"]
    confirm = input("Are you sure you want to delete '" + name + "'? (yes/no): ").strip().lower()

    if confirm == "yes":
        del students[roll]
        save_data(students)
        print("Student '" + name + "' deleted successfully.")
    else:
        print("Deletion cancelled.")

# Extra Feature - Show Top 3 Students

def show_toppers(students):
    """Show top 3 students by average marks."""
    print("\n--- Top 3 Students ---")
    if not students:
        print("No records available.")
        return

    sorted_students = sorted(students.items(), key=lambda x: x[1]["average"], reverse=True)

    count = 1
    for roll, data in sorted_students[:3]:
        print(str(count) + ". " + data["name"] + " | Average: " + str(data["average"]) + " | Grade: " + data["grade"])
        count += 1

# Main Menu

def main():
    print("=" * 45)
    print("    STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)

    students = load_data()

    while True:
        print("\n--- MENU ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Show Top 3 Students")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            show_toppers(students)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-7.")

if __name__ == "__main__":
    main()
