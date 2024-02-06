SIZE = int(input())
amount = 100    # Initial amount

matrix = []
gambler_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(SIZE):
    matrix.append(list(input()))

    if 'G' in matrix[row]:
        gambler_pos = row, matrix[row].index('G')
        matrix[row][gambler_pos[1]] = '-'


command = input()
while command != 'end':
    r = gambler_pos[0] + directions[command][0]
    c = gambler_pos[1] + directions[command][1]

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        print("Game over! You lost everything!")
        exit()

    element = matrix[r][c]
    matrix[r][c] = '-'
    gambler_pos = [r, c]

    if element == 'W':
        amount += 100

    elif element == 'P':
        amount -= 200
        if amount <= 0:
            print("Game over! You lost everything!")
            exit()

    elif element == 'J':
        amount += 100000
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {amount}$")
        break

    command = input()

else:
    print(f"End of the game. Total amount: {amount}$")

matrix[gambler_pos[0]][gambler_pos[1]] = 'G'
[print(''.join(row)) for row in matrix]
