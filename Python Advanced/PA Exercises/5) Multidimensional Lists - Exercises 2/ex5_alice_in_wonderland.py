n = int(input())

matrix = []
alice_pos = []  # [row, col]
tea_bags = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(n):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        alice_pos = [row, matrix[row].index('A')]
        matrix[row][alice_pos[1]] = '*'

while True:
    command = input()

    row, col = [
        alice_pos[0] + directions[command][0],
        alice_pos[1] + directions[command][1]
    ]

    if not (0 <= row < n and 0 <= col < n):
        break

    element = matrix[row][col]
    matrix[row][col] = '*'
    alice_pos = [row, col]

    if element == 'R':
        break
    elif element.isdigit():
        tea_bags += int(element)

    if tea_bags >= 10:
        break

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
[print(*row) for row in matrix]
