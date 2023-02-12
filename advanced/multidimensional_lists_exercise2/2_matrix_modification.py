def coordinates_are_valid(_matrix, row, col):
    if (0 <= int(row) < len(_matrix)) and (0 <= int(col) < len(_matrix)):
        return True
    else:
        return False


def add_func(_matrix, _, *args):
    row, col, value = args
    if not coordinates_are_valid(_matrix, int(row), int(col)):
        print('Invalid coordinates')
    else:
        _matrix[int(row)][int(col)] += int(value)
    return _matrix


def subtract_func(_matrix, _, *args):
    row, col, value = args
    if not coordinates_are_valid(_matrix, int(row), int(col)):
        print('Invalid coordinates')
    else:
        _matrix[int(row)][int(col)] -= int(value)
    return _matrix


def check_end_func(command, *args):
    if command == 'END':
        return True
    else:
        return False


def read_matrix(m_size):
    matrix = [[int(x) for x in input().split()] for _ in range(m_size)]
    return matrix


def print_matrix(matrix):
    return '\n'.join([' '.join(list(map(str, row))) for row in matrix])


def workflow(m_size):
    matrix = read_matrix(m_size)
    while True:
        commandline = input()
        if check_end_func(*commandline.split()):
            break
        else:
            if commandline.startswith('Add'):
                matrix = add_func(matrix, *commandline.split())
            elif commandline.startswith('Subtract'):
                matrix = subtract_func(matrix, *commandline.split())
    return print_matrix(matrix)


size = int(
    input())
print(workflow(size))
