command_line = input()
nested_dictionary = {}
while ':' in command_line:
    student, student_id, course = command_line.split(':')
    course = ''.join([x if x != ' ' else '_' for x in course])
    if course not in nested_dictionary:
        nested_dictionary[course] = {}
        nested_dictionary[course][student] = student_id
    else:
        nested_dictionary[course][student] = student_id
    command_line = input()
for name, number in nested_dictionary[command_line].items():
    print(f'{name} - {number}')

