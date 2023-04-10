def is_wall(row, col, lab):
    if lab[row][col] == '*':
        return True

    return False


def is_outside_lab(row, col, lab):
    if not 0 <= row < len(lab) or not 0 <= col < len(lab[0]):
        return True

    return False


def is_visited(row, col, lab):
    if lab[row][col] == 'v':
        return True

    return False


def is_exit(row, col, lab):
    if lab[row][col] == 'e':
        return True

    return False


def get_lab_paths(row, col, lab, direction, path):
    if is_outside_lab(row, col, lab) or is_visited(row, col, lab) or is_wall(row, col, lab):
        return

    path.append(direction)

    if is_exit(row, col, lab):
        print(*path, sep='')

    else:
        lab[row][col] = 'v'

        get_lab_paths(row, col + 1, lab, "R", path)
        get_lab_paths(row, col - 1, lab, "L", path)
        get_lab_paths(row - 1, col, lab, "U", path)
        get_lab_paths(row + 1, col, lab, "D", path)

        lab[row][col] = '-'

    path.pop()


rows, cols = [int(input()) for _ in range(2)]
labyrinth = []
for _ in range(rows):
    labyrinth.append(list(input()))

get_lab_paths(0, 0, labyrinth, '', [])
