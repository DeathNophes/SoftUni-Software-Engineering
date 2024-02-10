rows, cols = [int(x) for x in input().split(',')]

matrix = []
mouse_pos = []  # [row, col]
eaten_cheese = 0
total_cheese = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    matrix.append(list(input()))

    if 'M' in matrix[row]:
        mouse_pos = [row, matrix[row].index('M')]
        matrix[row][mouse_pos[1]] = '*'

    total_cheese += matrix[row].count('C')

while True:
    command = input()

    if command == 'danger':
        print("Mouse will come back later!")
        break

    new_row = directions[command][0] + mouse_pos[0]
    new_col = directions[command][1] + mouse_pos[1]

    if not 0 <= new_row < rows or not 0 <= new_col < cols:
        print("No more cheese for tonight!")
        break

    element = matrix[new_row][new_col]

    if element == 'C':
        eaten_cheese += 1
        matrix[new_row][new_col] = '*'
        mouse_pos = [new_row, new_col]
        if eaten_cheese == total_cheese:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif element == '@':
        continue

    elif element == 'T':
        print("Mouse is trapped!")
        mouse_pos = [new_row, new_col]
        break

    mouse_pos = [new_row, new_col]


matrix[mouse_pos[0]][mouse_pos[1]] = 'M'
[print(''.join(row)) for row in matrix]