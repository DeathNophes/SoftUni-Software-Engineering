quantity_of_decorations = int(input())
remaining_days = int(input())

Ornament_Set_price = 2
Tree_Skirt_price = 5
Tree_Garland_price = 3
Tree_Lights_price = 15

total_price = 0
total_spirit = 0

for day in range(1, remaining_days + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        total_price += quantity_of_decorations * Ornament_Set_price
        total_spirit += 5
    if day % 3 == 0:
        total_price += quantity_of_decorations * (Tree_Skirt_price + Tree_Garland_price)
        total_spirit += 3 + 10
    if day % 5 == 0:
        total_price += quantity_of_decorations * Tree_Lights_price
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30

    if day % 10 == 0:
        total_spirit -= 20
        total_price += Tree_Lights_price + Tree_Garland_price + Tree_Skirt_price
    if remaining_days % 10 == 0 and day == remaining_days:
        total_spirit -= 30

print(f"Total cost: {total_price}")
print(f"Total spirit: {total_spirit}")
