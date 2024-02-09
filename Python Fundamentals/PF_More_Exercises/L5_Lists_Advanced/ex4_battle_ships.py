n = int(input())
field = [input().split() for _ in range(n)]   # We create the battlefield (matrix)
destroyed_ships = 0

for i in range(len(field)):
    field[i] = list(map(int, field[i]))    # We turn str -> int

attack = input().split()

for wave in attack:
    curr_wave = wave.split('-')
    row = int(curr_wave[0])
    col = int(curr_wave[1])
    if field[row][col] != 0:
        field[row][col] -= 1
        if field[row][col] == 0:
            destroyed_ships += 1

print(destroyed_ships)
