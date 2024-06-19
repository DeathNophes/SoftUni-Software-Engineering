size = int(input())
car_number = input()

travel_distance = 0

car_pos = [0, 0]    # starting position
tunnels_pos = []    # [[row, col], [row, col]]

matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    matrix.append(input().split())

    if 'T' in matrix[row]:
        tunnels_pos.append([row, matrix[row].index('T')])


while True:
    command = input()
    if command == 'End':
        print(f"Racing car {car_number} DNF.")
        break

    new_row = car_pos[0] + directions[command][0]
    new_col = car_pos[1] + directions[command][1]

    element = matrix[new_row][new_col]
    car_pos = [new_row, new_col]

    if element == '.':
        travel_distance += 10

    elif element == 'T':
        car_pos = tunnels_pos[1]
        travel_distance += 30
        for row, col in tunnels_pos:
            matrix[row][col] = '.'

    elif element == 'F':
        print(f"Racing car {car_number} finished the stage!")
        travel_distance += 10
        break

matrix[car_pos[0]][car_pos[1]] = 'C'
print(f"Distance covered {travel_distance} km.")
[print(''.join(row)) for row in matrix]