n = int(input())
matrix = [[int(x) for x in input().split()] for row in range(n)]

command = input().split()
while command[0] != 'END':
    command_type = command[0]
    r, c, value = [int(x) for x in command[1:]]

    if not (0 <= r < n and 0 <= c < n):
        print("Invalid coordinates")
    elif command_type == 'Add':
        matrix[r][c] += value
    elif command_type == 'Subtract':
        matrix[r][c] -= value

    command = input().split()

[print(*row) for row in matrix]