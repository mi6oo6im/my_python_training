from collections import defaultdict

number_of_commands = int(input())
student_grade_dict = defaultdict(list)
for _ in range(number_of_commands):
    student, grade = input(), float(input())
    student_grade_dict[student].append(grade)

new_student_grade_dict = {k: sum(v) / len(v) for k, v in student_grade_dict.items() if sum(v) / len(v) >= 4.50}

[print(f'{k} -> {v:.2f}') for k, v in new_student_grade_dict.items()]
