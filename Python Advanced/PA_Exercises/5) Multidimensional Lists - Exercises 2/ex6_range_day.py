def move(direction: str, steps: int):
    """
    Returns the new position if the indices are valid and the new position is not a target
    """
    r = player_pos[0] + directions[direction][0] * steps
    c = player_pos[1] + directions[direction][1] * steps

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return player_pos

    if field[r][c] == 'x':
        return player_pos

    return [r, c]


def shoot(direction: str):
    """
    Returns the coordinates of the target if it exists
    otherwise returns None
    """
    r = player_pos[0] + directions[direction][0]
    c = player_pos[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]

    # We say to the bullet to keep going until it either hits a target or goes out of the field


SIZE = 5
field = []

total_targets = 0
targets_hit = 0

targets_hit_positions = []
player_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(SIZE):
    field.append(input().split())

    if 'A' in field[row]:
        player_pos = [row, field[row].index('A')]

    total_targets += field[row].count('x')

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'move':
        player_pos = move(command[1], int(command[2]))

    elif command[0] == 'shoot':
        target_down_pos = shoot(command[1])

        if target_down_pos:
            targets_hit_positions.append(target_down_pos)
            targets_hit += 1

        if targets_hit == total_targets:
            print(f"Training completed! All {total_targets} targets hit.")
            break

if targets_hit < total_targets:
    print(f"Training not completed! {total_targets - targets_hit} targets left.")
[print(row) for row in targets_hit_positions]
