def left_array_func(field, bunny):
    egg_array = []
    row, col = bunny
    egg_counter = 0
    for i in range(col - 1, -1, -1):
        if field[row][i] == 'X':
            break
        else:
            egg_array.append([row, i])
            egg_counter += field[row][i]
    return egg_array, egg_counter


def right_array_func(field, bunny):
    egg_array = []
    row, col = bunny
    egg_counter = 0
    for i in range(col + 1, len(field)):
        if field[row][i] == 'X':
            break
        else:
            egg_array.append([row, i])
            egg_counter += field[row][i]
    return egg_array, egg_counter


def up_array_func(field, bunny):
    egg_array = []
    row, col = bunny
    egg_counter = 0
    for i in range(row - 1, -1, -1):
        if field[i][col] == 'X':
            break
        else:
            egg_array.append([i, col])
            egg_counter += field[i][col]
    return egg_array, egg_counter


def down_array_func(field, bunny):
    egg_array = []
    row, col = bunny
    egg_counter = 0
    for i in range(row + 1, len(field)):
        if field[i][col] == 'X':
            break
        else:
            egg_array.append([i, col])
            egg_counter += field[i][col]
    return egg_array, egg_counter


def gameplay(field_size, directions_dict):
    field = []
    bunny_pos = None
    # build field and get bunny position
    for row in range(field_size):
        field.append([])
        field[row].extend([int(x) if x[-1].isdigit() else x for x in input().split()])
        if 'B' in field[row]:
            bunny_pos = (row, field[row].index('B'))
    # find the best direction
    highest_egg_count = float('-inf')
    direction_to_go = None
    collected_eggs_list = []
    current_egg_count = 0
    direction_eggs_list = []
    for direction in directions_dict.keys():
        if direction == 'up' and bunny_pos[0] > 0:
            direction_eggs_list, current_egg_count = up_array_func(field, bunny_pos)

        elif direction == 'down' and bunny_pos[0] < len(field) - 1:
            direction_eggs_list, current_egg_count = down_array_func(field, bunny_pos)

        elif direction == 'left' and bunny_pos[1] > 0:
            direction_eggs_list, current_egg_count = left_array_func(field, bunny_pos)

        elif direction == 'right' and bunny_pos[1] < len(field) - 1:
            direction_eggs_list, current_egg_count = right_array_func(field, bunny_pos)

        if current_egg_count > highest_egg_count:
            highest_egg_count = current_egg_count
            collected_eggs_list = direction_eggs_list
            direction_to_go = direction

    return direction_to_go, collected_eggs_list, highest_egg_count


DIRECTIONS = {
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
}
FIELD_SIZE = int(input())
preferable_direction, eggs_list, eggs_count = gameplay(FIELD_SIZE, DIRECTIONS)
print(preferable_direction)
if eggs_list:
    print(*eggs_list, sep='\n')
print(eggs_count)
