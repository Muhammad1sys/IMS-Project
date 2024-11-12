import re

print("Welcome to the Exam Department\nTo generate your exam report, please enter the following credentials:")

# Get and validate student's full name
student_name: str = input("Please enter your full name: ")
while not re.match("^[A-Za-z ]+$", student_name):
    print("Invalid input! Please enter a valid name.")
    student_name = input("Please enter your full name: ")

# Get and validate registration number
student_reg: str = input("Enter your registration number: ")
while not student_reg.isalnum():
    print("Invalid input! Please enter alphanumeric values only.")
    student_reg = input("Enter your registration number: ")

# Departments and degrees
departments = {
    '1. Computer Science': ['Bachelor of Science', 'Master of Science'],
    '2. Engineering': ['Bachelor of Science', 'Master of Science'],
    '3. Mathematics': ['Bachelor of Science', 'Master of Science'],
    '4. Physics': ['Bachelor of Science', 'Master of Science'],
    '5. Business Administration': ['Bachelor of Business Administration', 'Master of Business Administration']
}

def get_user_choice(prompt, options_count):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= options_count:
                return choice
            else:
                print(f"Please enter a number between 1 and {options_count}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Select department
print("Select your department:")
for dept in departments:
    print(dept)
dept_choice = get_user_choice("Enter the number of your choice: ", len(departments))
selected_department = list(departments.keys())[dept_choice - 1]

# Select degree program
print("\nSelect your degree program:")
for i, degree in enumerate(departments[selected_department], 1):
    print(f"{i}. {degree}")
degree_choice = get_user_choice("Enter the number of your choice: ", len(departments[selected_department]))
selected_degree = departments[selected_department][degree_choice - 1]

def calculate_grade(marks: float) -> str:
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

# Initialize empty dictionary to store subject, marks, and grades
exam_report = {}

# Get number of subjects from user
while True:
    try:
        no_of_subjects: int = int(input("Enter number of subjects studied (e.g., 5): "))
        if no_of_subjects > 0:
            break
        else:
            print("Number of subjects should be a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Get subject names and marks
for _ in range(no_of_subjects):
    subject: str = input('Enter the subject name: ')
    while True:
        try:
            marks: float = float(input(f'Enter the marks obtained in {subject}: '))
            break
        except ValueError:
            print('Please enter a valid number for marks.')

    # Calculate grade for each subject
    grade = calculate_grade(marks)
    # Store marks and grades in dictionary
    exam_report[subject] = {'marks': marks, 'grade': grade}

# Calculate overall grade
total_marks = sum(info['marks'] for info in exam_report.values())
average_marks = total_marks / no_of_subjects
overall_grade = calculate_grade(average_marks)

# Generate and print the exam report
print(f"{'Exam Report':^70}")
print(f"{'Name:':<20} {student_name.upper():<30} {'Reg#:':<10} {student_reg}")
print(f"{'Department:':<20} {selected_department:<30} {'Degree Program:':<20} {selected_degree}")

print("\n" + "-"*90)

# Header for subject report
print(f"{'Subject':<25} {'Marks':<10} {'Grade':<5}")

# Print each subject's information
for subject, info in exam_report.items():
    print(f"{subject.upper():<25} {info['marks']:<10} {info['grade']:<5}")

print("\n" + "-"*90)
print(f"{'Overall Average Marks:':<25} {average_marks:<10.2f} {'Overall Grade:':<15} {overall_grade}")
