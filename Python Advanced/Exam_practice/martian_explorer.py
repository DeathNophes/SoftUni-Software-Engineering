SIZE = 6

field = []
rover_pos = []

water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(SIZE):
    field.append(input().split())

    if 'E' in field[row]:
        rover_pos = [row, field[row].index('E')]
        field[row][rover_pos[1]] = '-'

commands = input().split(', ')

for command in commands:

    new_row = rover_pos[0] + directions[command][0]
    new_col = rover_pos[1] + directions[command][1]

    if new_row < 0:
        new_row = SIZE - 1
    elif new_row == SIZE:
        new_row = 0

    if new_col < 0:
        new_col = SIZE - 1
    elif new_col == SIZE:
        new_col = 0

    element = field[new_row][new_col]
    rover_pos = [new_row, new_col]
    field[new_row][new_col] = '-'

    if element == 'W':
        print(f"Water deposit found at ({new_row}, {new_col})")
        water_deposit += 1

    elif element == 'M':
        print(f"Metal deposit found at ({new_row}, {new_col})")
        metal_deposit += 1

    elif element == 'C':
        print(f"Concrete deposit found at ({new_row}, {new_col})")
        concrete_deposit += 1

    elif element == 'R':
        print(f"Rover got broken at ({new_row}, {new_col})")
        break

if water_deposit and metal_deposit and concrete_deposit:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
