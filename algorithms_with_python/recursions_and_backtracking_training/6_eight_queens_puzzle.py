def is_under_attack(row, col, rows, cols, left_diagonals, right_diagonals):
    if row in rows or col in cols or row - col in left_diagonals or row + col in right_diagonals:
        return True

    return False


def print_board(matrix):
    [print(*row, sep=' ') for row in matrix]
    print()
    return


def set_queen(row, col, board, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = '*'
    rows.add(row)
    cols.add(col)
    left_diagonals.add(row - col)
    right_diagonals.add(row + col)


def remove_queen(row, col, board, rows, cols, left_diagonals, right_diagonals):
    board[row][col] = '-'
    rows.remove(row)
    cols.remove(col)
    left_diagonals.remove(row - col)
    right_diagonals.remove(row + col)


def eight_queens_func(row, board, rows, cols, left_diagonals, right_diagonals):
    if row == 8:
        print_board(board)

    for col in range(len(board)):
        if not is_under_attack(row, col, rows, cols, left_diagonals, right_diagonals):
            set_queen(row, col, board, rows, cols, left_diagonals, right_diagonals)

            eight_queens_func(row + 1, board, rows, cols, left_diagonals, right_diagonals)

            remove_queen(row, col, board, rows, cols, left_diagonals, right_diagonals)


side = 8
chess_board = [['-'] * side for _ in range(side)]
eight_queens_func(0, chess_board, set(), set(), set(), set())

