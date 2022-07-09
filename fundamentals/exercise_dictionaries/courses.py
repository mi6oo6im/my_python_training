from collections import defaultdict

command_line = input()
course_dict = defaultdict(list)
while command_line != 'end':
    course, student = command_line.split(' : ')
    course_dict[course].append(student)
    command_line = input()

print(''.join([f'{k}: {len(v)}\n' + ''.join([f'-- {s}\n' for s in v]) for k, v in course_dict.items()]))

