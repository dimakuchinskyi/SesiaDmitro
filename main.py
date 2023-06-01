student_grades = {}
def create_student_grades():
    while True:
        student_name = input("Введіть ім'я студента (або введіть 'кінець' для завершення рахування студентів): ")
        if student_name == 'кінець':
            break
        grade = input("Введіть оцінку студента {}: ".format(student_name))
        student_grades[student_name] = int(grade)
def find_student_with_highest_grade():
    highest_grade = max(student_grades.values())
    for student, grade in student_grades.items():
        if grade == highest_grade:
            return student
create_student_grades()
student_with_highest_grade = find_student_with_highest_grade()
print("Студент з найвищою оцінкою: ", student_with_highest_grade)
