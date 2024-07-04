# Create an empty dictionary to store student names and their grades
student_grades = {}

# Get the number of students
num_students = int(input("Enter the number of students: "))

# Iterate through each student
for i in range(num_students):
    student_name = input(f"Enter the name of student {i + 1}: ")
    
    # Create an empty list to store the grades for this student
    grades = []
    
    # Get grades from the user
    num_grades = int(input(f"How many grades for {student_name}? "))
    for j in range(num_grades):
        grade = float(input(f"Enter grade {j + 1} for {student_name}: "))
        grades.append(grade)
    
    # Calculate the average grade for this student
    average_grade = sum(grades) / len(grades)
    
    # Assign a letter grade based on the average
    if average_grade >= 90:
        letter_grade = 'A'
    elif average_grade >= 80:
        letter_grade = 'B'
    elif average_grade >= 70:
        letter_grade = 'C'
    elif average_grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    
    # Store the student's name, grades, average, and letter grade in the dictionary
    student_grades[student_name] = {
        'grades': grades,
        'average_grade': average_grade,
        'letter_grade': letter_grade
    }

# Display the results
print("\nStudent Grades:")
for student, data in student_grades.items():
    print(f"Name: {student}")
    print(f"Grades: {data['grades']}")
    print(f"Average Grade: {data['average_grade']:.2f}")
    print(f"Letter Grade: {data['letter_grade']}\n")