def right_down_recursion(row, col, rows, cols):
    # check if cell is inbound
    if row >= rows or col >= cols:
        return 0
    # check if we have reached the base case
    if row == rows - 1 and col == cols - 1:
        return 1

    path_count = 0

    path_count += right_down_recursion(row, col + 1, rows, cols)
    path_count += right_down_recursion(row + 1, col, rows, cols)

    return path_count


rows, cols = [int(input()) for _ in range(2)]
print(right_down_recursion(0, 0, rows, cols))
