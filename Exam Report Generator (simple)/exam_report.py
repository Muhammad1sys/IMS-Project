print("Welcome to the Exam Department\nTo generate your exam report, please enter the following credentials:")

student_name: str = input("Please enter your full name: ")

student_reg: str = input("Enter your registration number: ")

departments = {
    '1. Computer Science': ['Bachelor of Science', 'Master of Science'],
    '2. Engineering': ['Bachelor of Science', 'Master of Science'],
    '3. Mathematics': ['Bachelor of Science', 'Master of Science'],
    '4. Physics': ['Bachelor of Science', 'Master of Science'],
    '5. Business Administration': ['Bachelor of Business Administration', 'Master of Business Administration']
}
print(departments.keys())
select_department: str = input("Write department name from above: ")
print(departments.values())
select_degree: str = input("Write the respective degree program as above mentioned: ")

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

# Initializing empty dictionary to store subject, marks, and grades
exam_report = {}

# Get number of subjects from user
while True:
    try:
        no_of_subjects: int = int(input("Enter number of subjects studied (e.g., 5): "))
        break
    except ValueError:
        print("Invalid input! Please enter an integer.")

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

# Generating overall grade
total_marks = sum(info['marks'] for info in exam_report.values())
average_marks = total_marks / no_of_subjects
overall_grade = calculate_grade(average_marks)

# Generating and printing the exam report
print(f"{'Exam Report':^70}")
print(f"{'Name:':<20} {student_name.upper():<30} {'Reg#:':<10} {student_reg}")
print(f"{'Department:':<20} {select_department.upper():<30} {'Degree Program:':<20} {select_degree.upper()}")

print("\n" + "-"*80)

# Header for subject report
print(f"{'Subject':<25} {'Marks':<10} {'Grade':<5}")

# Print each subject's information
for subject, info in exam_report.items():
    print(f"{subject.upper():<25} {info['marks']:<10} {info['grade']:<5}\n")

print("\n" + "-"*80)
print(f"{'Overall Average Marks:':<25} {average_marks:<10.2f} {'Overall Grade:':<15} {overall_grade}")