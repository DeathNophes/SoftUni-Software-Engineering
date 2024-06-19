size = int(input())

battlefield = []
sub_pos = []

destroyed_ships = 0
health = 3

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    battlefield.append(list(input()))

    if 'S' in battlefield[row]:
        sub_pos = [row, battlefield[row].index('S')]
        battlefield[row][sub_pos[1]] = '-'

while True:
    command = input()

    new_row = sub_pos[0] + directions[command][0]
    new_col = sub_pos[1] + directions[command][1]

    element = battlefield[new_row][new_col]
    sub_pos = [new_row, new_col]
    battlefield[new_row][new_col] = '-'

    if element == 'C':
        destroyed_ships += 1
        if destroyed_ships == 3:
            break

    elif element == '*':
        health -= 1
        if health == 0:
            break


if destroyed_ships == 3:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

if health == 0:
    row, col = sub_pos[0], sub_pos[1]
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")

battlefield[sub_pos[0]][sub_pos[1]] = 'S'
[print(''.join(row)) for row in battlefield]