from collections import deque

SIZE = 6
matrix = []

rest_counters = {
    'Tom': 0,
    'Jerry': 0
}

players = input().split(', ')
player_turn = 0     # 1, 2 -> 0, 1

for row in range(SIZE):
    matrix.append(input().split())

while True:
    position = input()
    row, col = int(position[1]), int(position[4])

    if rest_counters[players[player_turn]] == 0:
        element = matrix[row][col]

        if element == 'E':
            print(f"{players[player_turn]} found the Exit and wins the game!")
            break

        elif element == 'T':
            loser = players[player_turn]
            players.remove(players[player_turn])
            winner = players[0]

            print(f"{loser} is out of the game! The winner is {winner}.")
            break

        elif element == 'W':
            print(f"{players[player_turn]} hits a wall and needs to rest.")
            rest_counters[players[player_turn]] += 1

    else:
        rest_counters[players[player_turn]] -= 1

    player_turn += 1
    if player_turn == 2:
        player_turn = 0
