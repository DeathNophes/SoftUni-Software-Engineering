size = int(input())

matrix = []
jet_pos = []    # [row, col]

armor_value = 300
defeated_enemies = 0
total_enemies = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    matrix.append(list(input()))

    if 'J' in matrix[row]:
        jet_pos = [row, matrix[row].index('J')]
        matrix[row][jet_pos[1]] = '-'

    total_enemies += matrix[row].count('E')

while True:
    command = input()

    new_row = jet_pos[0] + directions[command][0]
    new_col = jet_pos[1] + directions[command][1]

    element = matrix[new_row][new_col]
    jet_pos = [new_row, new_col]
    matrix[new_row][new_col] = '-'

    if element == 'R':
        armor_value = 300

    elif element == 'E':
        defeated_enemies += 1
        if defeated_enemies == total_enemies:
            print("Mission accomplished, you neutralized the aerial threat!")
            break

        armor_value -= 100
        if armor_value == 0:
            row, col = jet_pos
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!")
            break

matrix[jet_pos[0]][jet_pos[1]] = 'J'
[print(''.join(row)) for row in matrix]
