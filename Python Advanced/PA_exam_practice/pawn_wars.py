def numerate_field_boxes(_row, _col):
    number = str(chr(97 + _col))
    number += str(SIZE - _row)
    return number


def can_we_take_pawn(curr_turn):
    possible_directions = {
        'black': [(1, 1), (1, -1)],
        'white': [(-1, -1), (-1, 1)]
    }

    if pawns[curr_turn] == 'w':
        for direction in possible_directions['white']:
            _row, _col = direction
            if white_pos[0] + _row == black_pos[0] and white_pos[1] + _col == black_pos[1]:
                return True

    elif pawns[curr_turn] == 'b':
        for direction in possible_directions['black']:
            _row, _col = direction
            if black_pos[0] + _row == white_pos[0] and black_pos[1] + _col == white_pos[1]:
                return True

    return False


def take_pawn(pawn_color):
    if pawn_color == 'black':
        white_pos[0], white_pos[1] = black_pos[0], black_pos[1]

    elif pawn_color == 'white':
        black_pos[0], black_pos[1] = white_pos[0], white_pos[1]


SIZE = 8

pawns = ['w', 'b']
turn = 0    # 1, 2 -> 0, 1

board = []

black_pos = []
white_pos = []

directions = {
    'white': (-1, 0),
    'black': (1, 0)
}

for row in range(SIZE):
    board.append(input().split())

    if 'w' in board[row]:
        white_pos = [row, board[row].index('w')]
        board[row][white_pos[1]] = '-'

    if 'b' in board[row]:
        black_pos = [row, board[row].index('b')]
        board[row][black_pos[1]] = '-'

while True:

    if turn == 0:

        if can_we_take_pawn(turn):
            take_pawn('black')
            print(f"Game over! White win, capture on {numerate_field_boxes(white_pos[0], white_pos[1])}.")
            exit()

        new_row = white_pos[0] + directions['white'][0]
        new_col = white_pos[1] + directions['white'][1]
        white_pos = [new_row, new_col]

        if white_pos[0] == 0:
            print(f"Game over! White pawn is promoted to a queen at {numerate_field_boxes(white_pos[0], white_pos[1])}.")
            exit()

    elif turn == 1:

        if can_we_take_pawn(turn):
            take_pawn('white')
            print(f"Game over! Black win, capture on {numerate_field_boxes(black_pos[0], black_pos[1])}.")
            exit()

        new_row = black_pos[0] + directions['black'][0]
        new_col = black_pos[1] + directions['black'][1]
        black_pos = [new_row, new_col]

        if black_pos[0] == 7:
            print(f"Game over! Black pawn is promoted to a queen at {numerate_field_boxes(black_pos[0], black_pos[1])}.")
            exit()

    turn += 1
    if turn == 2:
        turn = 0
