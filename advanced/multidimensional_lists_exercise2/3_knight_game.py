def is_valid_attack(board, attack_row, attack_col):
    if 0 <= attack_row < len(board) and 0 <= attack_col < len(board):
        return True
    else:
        return False


def count_knight_attacks(board, knights, attacks_range):
    most_attacks = float('-inf')
    knight_with_most_attacks = None
    for knight in knights:
        row, col = knight
        counter = 0
        for attack in attacks_range:
            change_row, change_col = attack
            attack_row = row + change_row
            attack_col = col + change_col
            if not is_valid_attack(board, attack_row, attack_col):
                continue
            if board[attack_row][attack_col] == 'K':
                counter += 1
        if most_attacks < counter:
            most_attacks = counter
            knight_with_most_attacks = (row, col)
    return knight_with_most_attacks, most_attacks


def remove_knight_from_board(board, knight, all_knights):
    row, col = knight
    board[row][col] = '0'
    all_knights.pop(all_knights.index(knight))
    return board, all_knights


def workflow(board_size, attacks):
    knights_locations = []
    board = []
    # create the board and collect knights' locations
    for row in range(board_size):
        board.append([])
        board[row].extend(list(input()))
        for col, cell in enumerate(board[row]):
            if cell == 'K':
                knights_locations.append((row, col))
    removed_knights = 0
    while True:
        # find the knight with most attacks
        knight_with_most, attacks_count = count_knight_attacks(board, knights_locations, attacks)
        # count removed knights
        if attacks_count == 0:
            return removed_knights
        board, knights_locations = remove_knight_from_board(board, knight_with_most, knights_locations)
        removed_knights += 1


KNIGHT_ATTACKS = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
BOARD_SIZE = int(input())
print(workflow(BOARD_SIZE, KNIGHT_ATTACKS))
