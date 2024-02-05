class FullColumnError(Exception):
    pass


class InvalidColumnChoice(Exception):
    pass


class BoardIsFull(Exception):
    pass


ROWS = 6
COLS = 7
MAXIMUM_CONNECTIONS = 4

DIRECTION_MAPPER = {
    'left': (0, -1),
    'up': (-1, 0),
    'main_diagonal': (-1, -1),
    'anti_diagonal': (-1, 1)
}


def print_board(_board):
    [print(row) for row in _board]


def get_first_available_row(col_index, _board):
    for row_index in range(ROWS - 1, -1, -1):
        if _board[row_index][col_index] == 0:
            return row_index
    else:
        raise FullColumnError


def validate_column_choice(col):
    if 1 <= col <= COLS:
        return True
    raise InvalidColumnChoice


def travel_opposite_direction(coordinates, _board, el_row, el_col, element):
    count = 0
    try:
        curr_row = el_row
        curr_col = el_col
        for _ in range(1, 4):
            next_element_row_index = curr_row + -(coordinates[0])
            next_element_col_index = curr_col + -(coordinates[1])

            if next_element_row_index < 0 or next_element_col_index < 0:
                return count

            if _board[next_element_row_index][next_element_col_index] != element:
                return count

            count += 1

            curr_row = next_element_row_index
            curr_col = next_element_col_index

        return count

    except IndexError:
        return count


def travel_direction(coordinates, _board, el_row, el_col, element):
    count = 0
    try:
        curr_row = el_row
        curr_col = el_col
        for _ in range(1, 4):
            next_element_row_index = curr_row + coordinates[0]
            next_element_col_index = curr_col + coordinates[1]

            if next_element_row_index < 0 or next_element_col_index < 0:
                return count

            if _board[next_element_row_index][next_element_col_index] != element:
                return count

            count += 1

            curr_row = next_element_row_index
            curr_col = next_element_col_index

        return count

    except IndexError:
        return count


def is_board_full(_board):
    return ROWS * COLS < turns


def is_winner(curr_row_index, curr_col_index, _board):
    searched_el = _board[curr_row_index][curr_col_index]
    for direction, coordinates in DIRECTION_MAPPER.items():
        count_1 = travel_direction(coordinates, _board, curr_row_index, curr_col_index, searched_el)
        count_2 = travel_opposite_direction(coordinates, _board, curr_row_index, curr_col_index, searched_el)
        if count_1 + count_2 + 1 >= MAXIMUM_CONNECTIONS:
            return True
    else:
        return False


board = [[0 for _ in range(COLS)] for row in range(ROWS)]

turns = 1
while True:
    player = 2 if turns % 2 == 0 else 1

    try:
        column = int(input(f"Player {player}, please choose a column"))
        validate_column_choice(column)
        column_index = column - 1
        row = get_first_available_row(column_index, board)
        board[row][column_index] = player
        if is_winner(row, column_index, board):
            break
        if is_board_full(turns):
            print("Board is full! Nobody wins!")
            exit()
    except (InvalidColumnChoice, ValueError):
        print(f"This column is invalid, please select a number between 1 and {COLS}")
        continue
        # The player must enter a valid number (int) in order to play
    except FullColumnError:
        print("This column is full, please select another one")
        continue
        # The player changes when we add to the turns,
        # when we don't do it the turn remains the same as does the player

    print_board(board)
    turns += 1

print_board(board)
print(f"WINNER is Player {player}")
