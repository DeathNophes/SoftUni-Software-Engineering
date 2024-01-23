def find_player_position():
    for row in range(rows):
        if 'P' in matrix[row]:
            return row, matrix[row].index('P')


def check_valid_index(row, col, player=False):
    global wins     # We take this from the global scope so we can change it
    if 0 <= row < rows and 0 <= col < cols:
        return True
    if player:
        wins = True


def bunnies_position():
    positions = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'B':
                positions.append([row, col])
    return positions


def bunnies_move(bunnies_pos):
    for row, col in bunnies_pos:   # We iterate through every bunny and unpack the list [row, col]
        for bunnie_move in directions.values(): # [(-1, 0), (1, 0), (0, -1), (0, 1)]
            new_row = row + bunnie_move[0]
            new_col = col + bunnie_move[1]

            if check_valid_index(new_row, new_col):
                matrix[new_row][new_col] = 'B'


def check_player_alive(row, col):
    if matrix[row][col] == 'B':
        show_results(status='dead')


def show_results(status='won'):
    [print(*row, sep='') for row in matrix]
    print(f"{status}: {player_row} {player_col}")

    raise SystemExit


rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]
commands = input()
wins = False

directions = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

player_row, player_col = find_player_position()
matrix[player_row][player_col] = '.'

for command in commands:
    player_movement_row = player_row + directions[command][0]
    player_movement_col = player_col + directions[command][1]

    if check_valid_index(player_movement_row, player_movement_col, True):
        player_row = player_movement_row
        player_col = player_movement_col
        # We move the player

    bunnies_move(bunnies_position())

    if wins:
        show_results()

    check_player_alive(player_row, player_col)