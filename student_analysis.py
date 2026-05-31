# =========================================================
# SMART CAMPUS INFORMATION SYSTEM
# =========================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# 1. STUDENT REGISTRATION AND GRADE EVALUATION
# =========================================================
def student_registration():
    print("========== STUDENT REGISTRATION ==========")

    student_name = input("Enter student name: ")
    score = float(input("Enter exam score (0-100): "))

    if score >= 90 and score <= 100:
        grade = "A"
        remark = "Excellent"

    elif score >= 75:
        grade = "B"
        remark = "Very Good"

    elif score >= 60:
        grade = "C"
        remark = "Good"

    elif score >= 40:
        grade = "D"
        remark = "Average"

    else:
        grade = "F"
        remark = "Needs Improvement"

    print("\n--- Student Report ---")
    print("Name:", student_name)
    print("Score:", score)
    print("Grade:", grade)
    print("Performance Remark:", remark)

# =========================================================
# 2. COURSE ENROLLMENT MANAGEMENT SYSTEM
# =========================================================
def course_enrollment():
    print("\n========== COURSE ENROLLMENT ==========")

    courses = []
    max_courses = 5

    while True:

        if len(courses) >= max_courses:
            print("Maximum course limit reached!")
            break

        course_name = input("Enter course name (or 'done' to finish): ")

        if course_name.lower() == "done":
            break

        credits = input("Enter credit value: ")

        if not credits.isdigit():
            print("Invalid credit value!")
            continue

        credits = int(credits)

        if credits <= 0:
            print("Credit must be positive!")
            continue

        courses.append((course_name, credits))

        print(f"Course '{course_name}' added successfully.\n")

    print("\n--- Enrollment Report ---")

    for course, credit in courses:
        print(f"Course: {course}, Credits: {credit}")

    print("Total courses enrolled:", len(courses))

# =========================================================
# 3. STUDENT RECORD STORAGE AND MANAGEMENT
# =========================================================
def student_records():
    print("\n========== STUDENT RECORDS ==========")

    students = []

    students.append({"name": "Priya", "age": 20, "grades": [85, 90, 78]})
    students.append({"name": "Rahul", "age": 21, "grades": [72, 88, 91]})
    students.append({"name": "Anita", "age": 19, "grades": [95, 89, 92]})

    for student in students:

        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Grades:", student["grades"])
        print("-----------------------")

    # Event Participation Analysis

    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}

    common_participants = event_A & event_B
    all_participants = event_A | event_B
    only_event_A = event_A - event_B

    print("\n=== Event Participation Analysis ===")

    print("Common Participants:", common_participants)
    print("All Participants:", all_participants)
    print("Only Event A Participants:", only_event_A)

# =========================================================
# 4. SEARCHING AND SORTING STUDENT DATA
# =========================================================
def sorting_searching():
    print("\n========== SEARCHING AND SORTING ==========")

    student_ids = [105, 102, 110, 108, 101, 115]

    print("Original IDs:", student_ids)

    # Bubble Sort

    n = len(student_ids)

    for i in range(n):

        for j in range(0, n - i - 1):

            if student_ids[j] > student_ids[j + 1]:

                temp = student_ids[j]
                student_ids[j] = student_ids[j + 1]
                student_ids[j + 1] = temp

    print("Sorted IDs (Bubble Sort):", student_ids)

    # Selection Sort

    student_ids2 = [105, 102, 110, 108, 101, 115]

    n = len(student_ids2)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if student_ids2[j] < student_ids2[min_index]:
                min_index = j

        temp = student_ids2[i]
        student_ids2[i] = student_ids2[min_index]
        student_ids2[min_index] = temp

    print("Sorted IDs (Selection Sort):", student_ids2)

    # Linear Search

    target = 108
    found_index = -1

    for i in range(len(student_ids2)):

        if student_ids2[i] == target:
            found_index = i
            break

    if found_index != -1:
        print("Linear Search: ID", target, "found at index", found_index)

    else:
        print("Linear Search: ID not found")

    # Binary Search

    low = 0
    high = len(student_ids) - 1
    found_index = -1

    while low <= high:

        mid = (low + high) // 2

        if student_ids[mid] == target:
            found_index = mid
            break

        elif student_ids[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    if found_index != -1:
        print("Binary Search: ID", target, "found at index", found_index)

    else:
        print("Binary Search: ID not found")

# =========================================================
# 5. STUDENT FEE CALCULATION USING FUNCTIONS
# =========================================================
def fee_calculation():
    print("\n========== STUDENT FEE CALCULATION ==========")

    def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):

        total_fee = tuition_fee + hostel_fee + transportation_fee

        return total_fee

    # Case 1

    total1 = calculate_fee(50000)

    print("Total Fee (Tuition only):", total1)

    # Case 2

    total2 = calculate_fee(50000, hostel_fee=30000)

    print("Total Fee (Tuition + Hostel):", total2)

    # Case 3

    total3 = calculate_fee(
        50000,
        hostel_fee=30000,
        transportation_fee=10000
    )

    print("Total Fee (Tuition + Hostel + Transport):", total3)

# =========================================================
# 6. FILE-BASED ACADEMIC RECORD MANAGEMENT
# =========================================================
def file_management():
    print("\n========== FILE MANAGEMENT ==========")

    with open("student_records.txt", "w") as file:

        file.write("ID,Name,Marks\n")
        file.write("101,Arjun,85\n")
        file.write("102,Meera,92\n")
        file.write("103,Ravi,76\n")
        file.write("104,Anita,89\n")

    print("Student records written successfully.")

    print("\nReading stored records:")

    with open("student_records.txt", "r") as file:

        records = file.readlines()

        for record in records:
            print(record.strip())

    print("\nGenerating Report:")

    total_students = 0
    total_marks = 0
    highest_marks = -1
    top_student = ""

    for record in records[1:]:

        parts = record.strip().split(",")

        student_id = parts[0]
        name = parts[1]
        marks = int(parts[2])

        total_students += 1
        total_marks += marks

        if marks > highest_marks:
            highest_marks = marks
            top_student = name

    average_marks = total_marks / total_students

    print("Total Students:", total_students)
    print("Average Marks:", average_marks)
    print("Top Student:", top_student, "with", highest_marks, "marks")

# =========================================================
# 7. DIRECTORY SCANNING WITH EXCEPTION HANDLING
# =========================================================
def directory_scanning():
    print("\n========== DIRECTORY SCANNING ==========")

    class MissingFileOrFolderError(Exception):
        """Raised when a folder is empty."""
        pass

    def scan_directory(path):

        try:

            if not os.path.exists(path):
                raise FileNotFoundError(
                    f"Invalid directory path: {path}"
                )

            print(f"\nScanning directory: {path}\n")

            for root, dirs, files in os.walk(path):

                level = root.replace(path, "").count(os.sep)

                indent = " " * 4 * level

                print(f"{indent}{os.path.basename(root)}/")

                sub_indent = " " * 4 * (level + 1)

                for f in files:
                    print(f"{sub_indent}{f}")

                if not files and not dirs:
                    raise MissingFileOrFolderError(
                        f"Empty folder detected: {root}"
                    )

        except FileNotFoundError as e:
            print(f"Error: {e}")

        except MissingFileOrFolderError as e:
            print(f"Custom Error: {e}")

        except Exception as e:
            print(f"Unexpected Error: {e}")

    directory_path = input(
        "\nEnter directory path to scan: "
    )

    scan_directory(directory_path)

# =========================================================
# 8. STUDENT PERFORMANCE ANALYTICS
# =========================================================
def performance_analysis():
    print("\n========== STUDENT PERFORMANCE ANALYTICS ==========")

    try:

        df = pd.read_excel("C:\\Users\\Admin\\OneDrive\\Desktop\\tejuuu\\DAY1\\python\\student_performance.xlsx")

        print("\n--- Raw Data ---")
        print(df.head())

        print("\n--- Statistical Summary ---")
        print(df.describe())

        scores = df[["Math", "Science", "English"]].to_numpy()

        mean_scores = np.mean(scores, axis=0)
        median_scores = np.median(scores, axis=0)
        std_dev_scores = np.std(scores, axis=0)

        print("\n--- NumPy Analysis ---")

        print("Mean Scores:", mean_scores)
        print("Median Scores:", median_scores)
        print("Standard Deviation:", std_dev_scores)

        top_math = df.loc[df["Math"].idxmax(), "Name"]
        top_science = df.loc[df["Science"].idxmax(), "Name"]
        top_english = df.loc[df["English"].idxmax(), "Name"]

        print("\n--- Top Performers ---")

        print("Math:", top_math)
        print("Science:", top_science)
        print("English:", top_english)

        subjects = ["Math", "Science", "English"]

        plt.bar(subjects, mean_scores)

        plt.title("Average Scores per Subject")
        plt.xlabel("Subjects")
        plt.ylabel("Average Score")

        plt.show()

        df.plot(
            x="Name",
            y=["Math", "Science", "English"],
            kind="bar"
        )

        plt.title("Student Performance Comparison")
        plt.ylabel("Scores")

        plt.show()

    except FileNotFoundError:

        print(
            "Error: student_performance.csv file not found."
        )

    except Exception as e:

        print(f"Unexpected Error: {e}")



# ============================================================
# MAIN SYSTEM APPLICATION DASHBOARD
# ============================================================

while True:

    print("\n===================================")
    print(" SMART CAMPUS INFORMATION SYSTEM ")
    print("===================================")
    print("1. Student Registration")
    print("2. Course Enrollment")
    print("3. Student Record Management")
    print("4. Sorting and Searching")
    print("5. Fee Calculation")
    print("6. File Handling")
    print("7. Directory Scanning")
    print("8. Performance Analysis")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_registration()

    elif choice == "2":
        course_enrollment()

    elif choice == "3":
        student_records()

    elif choice == "4":
        sorting_searching()

    elif choice == "5":
        fee_calculation()

    elif choice == "6":
        file_management()

    elif choice == "7":
        directory_scanning()

    elif choice == "8":
        performance_analysis()

    elif choice == "9":
        print(
            "Exiting Smart Campus Information System..."
        )
        break

    else:
        print(
            "Invalid choice! Please try again."
        )
