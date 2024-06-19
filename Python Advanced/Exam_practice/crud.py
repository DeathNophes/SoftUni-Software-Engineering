SIZE = 6

matrix = []

for row in range(SIZE):
    matrix.append(input().split())

starting_pos = input()
row, col = int(starting_pos[1]), int(starting_pos[4])

player_pos = [row, col]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    line = input()
    if line == 'Stop':
        break

    command = line.split(', ')

    new_row = player_pos[0] + directions[command[1]][0]
    new_col = player_pos[1] + directions[command[1]][1]

    element = matrix[new_row][new_col]
    player_pos = [new_row, new_col]

    if command[0] == 'Create':
        value = command[2]
        if element == '.':
            matrix[new_row][new_col] = value

    elif command[0] == 'Update':
        value = command[2]
        if element != '.':
            matrix[new_row][new_col] = value

    elif command[0] == 'Delete':
        matrix[new_row][new_col] = '.'

    elif command[0] == 'Read':
        if element != '.':
            print(element)

[print(*row) for row in matrix]
