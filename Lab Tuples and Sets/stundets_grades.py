number_of_students = int(input())
students_grades = {}
for student in range(number_of_students):
    student_name, grade = input().split()
    if student_name not in students_grades:
        students_grades[student_name] = []
    students_grades[student_name].append(float(grade))

for student, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    grades_string = " ".join(map(lambda grade: f'{grade:.2f}', grades))
    print(f"{student} -> {grades_string} (avg: {average_grade:.2f})")
