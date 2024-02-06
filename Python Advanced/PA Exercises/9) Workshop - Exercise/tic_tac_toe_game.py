from collections import deque


def check_for_win():
    player_name, player_symbol = players[0].values()

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(SIZE)])
    anti_diagonal_win = all([board[i][SIZE - 1 - i] == player_symbol for i in range(SIZE)])
    # The other diagonal
    row_win = any([all([el == player_symbol for el in row]) for row in board])
    col_win = any([all([board[r][c] == player_symbol for r in range(SIZE)]) for c in range(SIZE)])

    if any([first_diagonal_win, anti_diagonal_win, row_win, col_win]):
        print_board()
        print(f"{player_name} won!")

        raise SystemExit


def place_symbol(row, col):
    board[row][col] = players[0]['symbol']

    check_for_win()
    print_board()

    if turns == SIZE * SIZE:
        print("Draw!")
        raise SystemExit

    players.rotate()


def choose_position():
    global turns

    while True:
        try:
            position = int(input(f"{players[0]['name']} choose a free position between [1-{SIZE * SIZE}]: "))
            row = (position - 1) // SIZE
            col = (position - 1) % SIZE
        except ValueError:
            print_valid_position_msg()
            continue

        if 1 <= position <= SIZE * SIZE and board[row][col] == " ":     # We first validate the position
            turns += 1
            place_symbol(row, col)
        else:
            print_valid_position_msg()


def print_valid_position_msg():
    print(f"{players[0]['name']} this is not a valid position")


def print_board():
    [print(f"| {' | '.join(row)} |") for row in board]


def print_game_state(begin=False):

    if begin:
        print("This is the numeration of the board: ")
        print_board()

        for row in range(SIZE):
            for col in range(SIZE):
                board[row][col] = " "

    else:
        print_board()


def start_game():
    player_one = input("Player one, please enter your name: ")
    player_two = input("Player two, please enter your name: ")

    while True:
        player_one_symbol = input(f"{player_one}, would you like to play with O or X?: ").upper()

        if player_one_symbol not in ['X', 'O']:
            print(f"{player_one}, please enter a valid symbol!")
        else:
            break

    player_two_symbol = 'O' if player_one_symbol == 'X' else 'X'

    players.append({'name': player_one, 'symbol': player_one_symbol})
    players.append({'name': player_two, 'symbol': player_two_symbol})

    print_game_state(begin=True)
    choose_position()


SIZE = 3
turns = 0

board = [[str(r + c) for c in range(SIZE)] for r in range(1, SIZE * SIZE + 1, SIZE)]
players = deque()
# We use deque so that the players can rotate between one another

start_game()
