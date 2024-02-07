rows, cols = [int(x) for x in input().split()]

field = []
player_pos = []
player_starting_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    field.append(list(input()))

    if 'B' in field[row]:
        player_pos = [row, field[row].index('B')]
        player_starting_pos = player_pos


while True:
    command = input()
    next_row = player_pos[0] + directions[command][0]
    next_col = player_pos[1] + directions[command][1]

    if not (0 <= next_row < rows and 0 <= next_col < cols):
        print("The delivery is late. Order is canceled.")
        field[player_starting_pos[0]][player_starting_pos[1]] = " "
        break

    element = field[next_row][next_col]

    if element == '*':
        continue

    elif element == '-':
        field[next_row][next_col] = '.'

    elif element == 'P':
        print("Pizza is collected. 10 minutes for delivery.")
        field[next_row][next_col] = 'R'

    elif element == 'A':
        print("Pizza is delivered on time! Next order...")
        field[next_row][next_col] = 'P'
        break

    player_pos = [next_row, next_col]

[print(''.join(row)) for row in field]