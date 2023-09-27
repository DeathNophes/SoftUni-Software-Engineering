group_size = int(input())
days = int(input())
current_coins = 0
for day in range(1, days + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    current_coins += 50
    current_coins -= group_size * 2
    if day % 3 == 0:
        current_coins -= group_size * 3
    if day % 5 == 0:
        current_coins += group_size * 20
        if day % 3 == 0:
            current_coins -= group_size * 2

coins_per_companion = int(current_coins / group_size)
print(f"{group_size} companions received {coins_per_companion} coins each.")
