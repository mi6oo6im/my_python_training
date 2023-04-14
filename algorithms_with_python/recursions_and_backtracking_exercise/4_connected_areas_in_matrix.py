class Area:
    def __init__(self, row: int, col: int, size: int):
        self.row = row
        self.col = col
        self.size = size


def explore_area(row_, col_, matrix_):
    if row_ < 0 or col_ < 0 or row_ >= len(matrix_) or col_ >= len(matrix_[0]):
        return 0

    if matrix_[row_][col_] != '-':
        return 0

    matrix_[row_][col_] = 'v'

    result = 1
    result += explore_area(row_ - 1, col_, matrix_)
    result += explore_area(row_ + 1, col_, matrix_)
    result += explore_area(row_, col_ - 1, matrix_)
    result += explore_area(row_, col_ + 1, matrix_)

    return result


rows = int(input())
cols = int(input())

matrix = []
for _ in range(rows):
    matrix.append(list(input()))

areas = []
for row in range(rows):
    for col in range(cols):
        result = explore_area(row, col, matrix)
        if result == 0:
            continue
        areas.append(Area(row, col, result))
sorted_areas = sorted(areas, key=lambda a: a.size, reverse=True)
print(f'Total areas found: {len(sorted_areas)}')

for idx, area in enumerate(sorted_areas):
    print(f'Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}')