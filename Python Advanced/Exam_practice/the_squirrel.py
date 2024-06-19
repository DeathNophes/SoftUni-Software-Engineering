size = int(input())
commands = input().split(', ')

matrix = []
squirrel_pos = []   # [row, col]
hazelnuts = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    matrix.append(list(input()))

    if 's' in matrix[row]:
        squirrel_pos = [row, matrix[row].index('s')]
        matrix[row][squirrel_pos[1]] = '*'


for command in commands:
    new_r = squirrel_pos[0] + directions[command][0]
    new_c = squirrel_pos[1] + directions[command][1]

    if not (0 <= new_r < size and 0 <= new_c < size):
        print("The squirrel is out of the field.")
        break

    element = matrix[new_r][new_c]
    squirrel_pos = [new_r, new_c]
    matrix[new_r][new_c] = '*'

    if element == 'h':
        hazelnuts += 1
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break

    elif element == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        break

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
