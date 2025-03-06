#  This program is manages the grade data for various students
student = {}

# Function to add the student name and scores
def add_student():
   name = input("Enter the student's name: ")
   scores = input("Enter the student's scores: ")
   scores = tuple(map(int, scores.split()))
   student[name] = scores
   print (f'{name} has been added successfully')

# function to get score
def get_score():
    name = input("Enter the student's name to get their score: ")
    print(student.get(name, "Student not found in DataBase\n"))

# Function that sorts the highest and lowest value
def highest_lowest_score():
    all_score = [score for scores in student.values() for score in scores]
    if all_score:
        print(f"Highest score = {max(all_score)}\nLowest score = {min(all_score)}\n")
    else:
        print("No score available yet\n")

# Function to display unique student names using a set
def unique_names():
    print('(unique names: ', set(student.keys()),"\n")

# Update the Students data in the dictionary
def update_student_score():
    name = input("Enter the name of the student you want to update: ")
    if name in student.keys():
        score = input("Enter the updated scores: ")
        score = tuple(map(int, score.split()))
        student[name] = score
        print(f"{name} has been updated successfully")
    else:
        print("Student does not exist in the dataBase! please try again")

def delete_student():
    name = input("Enter the student name to delete: ")
    try:
        del student[name]
        print("Student has been removed successfully: ")
    except:
        print("Student isn't found in the system! try again")

def check_studentInData():
    print(student.keys())

# Menu display option
import sys
def menu():
    print("""
    STUDENT GRADE MANAGEMENT SYSTEM
    -------------------------------
    """)
    while True:
        print("""
        1. Add Student
        2. Retrieve Score
        3. Find Highest and lowest score
        4. Display Students Unique name
        5. Update a student's data
        6. Delete a student and their scores
        7. Check the students saved
        8. Exit""","\n")

        choice = str((input("chose an option: ")))
        if choice == "1":
            add_student()
        elif choice == "2":
            get_score()
        elif choice == "3":
            highest_lowest_score()
        elif choice == "4":
            unique_names()
        elif choice == "8":
            print("Exiting program...")
            sys.exit()
        elif choice == "5":
            update_student_score()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            check_studentInData()
        else:
            print("Invalid choice! Please try again\n")
menu()