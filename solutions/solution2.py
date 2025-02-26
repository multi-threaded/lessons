# Initialize an empty dictionary to store student grades
grades = {}

# Function to add a student and their grade
def add_student(name, grade):
    grades[name] = grade
    print(f"Added {name} with grade {grade}.")

# Function to print all student grades
def print_grades():
    print("Grades:")
    for name, grade in grades.items():
        print(f"{name}: {grade}")

# Function to update a student's grade
def update_grade(name, new_grade):
    if name in grades:
        grades[name] = new_grade
        print(f"Updated {name}'s grade to {new_grade}.")
    else:
        print(f"Student {name} not found.")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Print Grades")
    print("3. Update Grade")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        student_name = input("Enter student name: ")
        student_grade = input("Enter student grade: ")
        add_student(student_name, student_grade)
    elif choice == '2':
        print_grades()
    elif choice == '3':
        student_name = input("Enter student name: ")
        new_grade = input("Enter new grade: ")
        update_grade(student_name, new_grade)
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")