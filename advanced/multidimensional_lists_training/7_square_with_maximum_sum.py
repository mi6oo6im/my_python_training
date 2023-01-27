rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
biggest_sum = float('-inf')
biggest_square_pos = None
for row in range(rows - 1):
    for col in range(cols - 1):
        current_cell = (row, col)
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            biggest_square_pos = current_cell

row, col = biggest_square_pos
print(matrix[row][col], matrix[row][col + 1])
print(matrix[row + 1][col], matrix[row + 1][col + 1])
print(biggest_sum)