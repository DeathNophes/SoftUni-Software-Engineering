rows, cols = [int(x) for x in input().split(', ')]

matrix = []
player_pos = []

my_items = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0
}

all_items_collected = False

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

collected_items, total_items = 0, 0

for row in range(rows):
    matrix.append(input().split())

    if 'Y' in matrix[row]:
        player_pos = [row, matrix[row].index('Y')]
        matrix[row][player_pos[1]] = 'x'

    total_items += matrix[row].count('C')
    total_items += matrix[row].count('D')
    total_items += matrix[row].count('G')


while True:
    line = input()
    if line == 'End':
        break

    line = line.split('-')
    command = line[0]
    steps = int(line[1])

    for _ in range(steps):
        new_row = player_pos[0] + directions[command][0]
        new_col = player_pos[1] + directions[command][1]

        if new_row < 0:
            new_row = rows - 1
        elif new_row == rows:
            new_row = 0

        if new_col < 0:
            new_col = cols - 1
        elif new_col == cols:
            new_col = 0

        element = matrix[new_row][new_col]
        player_pos = [new_row, new_col]
        matrix[new_row][new_col] = 'x'

        if element == 'C':
            my_items['Cookies'] += 1
            collected_items += 1

        elif element == 'G':
            my_items['Gifts'] += 1
            collected_items += 1

        elif element == 'D':
            my_items['Christmas decorations'] += 1
            collected_items += 1

        if collected_items == total_items:
            print("Merry Christmas!")
            all_items_collected = True
            break

    if all_items_collected:
        break

matrix[player_pos[0]][player_pos[1]] = 'Y'

print("You've collected:")
for key, value in my_items.items():
    print(f"- {value} {key}")

[print(*row) for row in matrix]

