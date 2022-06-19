curriculum_list = input().split(', ')
input_line = input()
while input_line != 'course start':
    command_list = input_line.split(':')
    command = command_list[0]
    if command == 'Add':
        new_course = command_list[1]
        if new_course not in curriculum_list:
            curriculum_list.append(new_course)
    elif command == 'Insert':
        new_course = command_list[1]
        index = int(command_list[2])
        if new_course not in curriculum_list:
            curriculum_list.insert(index, new_course)
    elif command == 'Remove':
        course_to_remove = command_list[1]
        if course_to_remove in curriculum_list:
            curriculum_list.remove(course_to_remove)
            if course_to_remove + '-Exercise' in curriculum_list:
                curriculum_list.remove(course_to_remove + '-Exercise')
    elif command == 'Swap':
        first_lesson_to_swap, second_lesson_to_swap = command_list[1], command_list[2]
        if first_lesson_to_swap in curriculum_list and second_lesson_to_swap in curriculum_list:
            if first_lesson_to_swap + '-Exercise' in curriculum_list and second_lesson_to_swap + \
                    '-Exercise' in curriculum_list:
                first_index = curriculum_list.index(first_lesson_to_swap)
                first_index_exercise = curriculum_list.index(first_lesson_to_swap) + 1
                second_index = curriculum_list.index(second_lesson_to_swap)
                second_index_exercise = curriculum_list.index(second_lesson_to_swap) + 1
                curriculum_list[first_index], curriculum_list[first_index_exercise] \
                    , curriculum_list[second_index], curriculum_list[second_index_exercise] \
                    = curriculum_list[second_index], curriculum_list[second_index_exercise] \
                    , curriculum_list[first_index], curriculum_list[first_index_exercise]
            else:
                first_index = curriculum_list.index(first_lesson_to_swap)
                second_index = curriculum_list.index(second_lesson_to_swap)
                curriculum_list[first_index], curriculum_list[second_index] = \
                    curriculum_list[second_index], curriculum_list[first_index]
            if first_lesson_to_swap + '-Exercise' in curriculum_list:
                curriculum_list.insert(second_index + 1, first_lesson_to_swap + '-Exercise')
                curriculum_list.pop(first_index + 1)
            if second_lesson_to_swap + '-Exercise' in curriculum_list:
                curriculum_list.pop(second_index + 1)
                curriculum_list.insert(first_index + 1, second_lesson_to_swap + '-Exercise')
    elif command == 'Exercise':
        lesson_to_add_exercise = command_list[1]
        if lesson_to_add_exercise in curriculum_list and not lesson_to_add_exercise + '-Exercise' in curriculum_list:
            exercise_index = curriculum_list.index(lesson_to_add_exercise) + 1
            curriculum_list.insert(exercise_index, lesson_to_add_exercise + '-Exercise')
        elif lesson_to_add_exercise not in curriculum_list:
            curriculum_list.append(lesson_to_add_exercise)
            curriculum_list.append(lesson_to_add_exercise + '-Exercise')
    input_line = input()
curriculum_list_numbered = [f'{x + 1}.{curriculum_list[x]}' for x in range(0, len(curriculum_list))]
print(*curriculum_list_numbered, sep='\n')
