students_count = int(input())
students = {}
for _ in range(students_count):
    name, grade = input().split()
    if name not in students.keys():
        students[name] = []
    students[name].append(float(grade))
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    grades_str = ' '.join(f'{num:.2f}' for num in grades)
    print(f'{name} -> {grades_str} (avg: {avg:.2f})')
