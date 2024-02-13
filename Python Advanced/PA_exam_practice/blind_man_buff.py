rows, cols = [int(x) for x in input().split()]

matrix = []
player_pos = []

turns = 0
players_touched = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        player_pos = [row, matrix[row].index('B')]
        matrix[row][player_pos[1]] = '-'


while True:
    command = input()
    if command == 'Finish':
        break

    if players_touched == 3:
        break

    new_row = player_pos[0] + directions[command][0]
    new_col = player_pos[1] + directions[command][1]

    if not (0 <= new_row < rows and 0 <= new_col < cols):
        continue

    element = matrix[new_row][new_col]

    if element == 'P':
        players_touched += 1
        turns += 1

    elif element == 'O':
        continue

    elif element == '-':
        turns += 1

    player_pos = [new_row, new_col]
    matrix[new_row][new_col] = '-'


print("Game over!")
print(f"Touched opponents: {players_touched} Moves made: {turns}")