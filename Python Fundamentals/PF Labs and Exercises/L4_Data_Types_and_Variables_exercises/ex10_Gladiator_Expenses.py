lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0
shield_broken_counter = 0

for lost_fight in range(1, lost_fights + 1):
    if lost_fight % 2 == 0:
        total_expenses += helmet_price
    if lost_fight % 3 ==0:
        total_expenses += sword_price
    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        total_expenses += shield_price
        shield_broken_counter += 1
        if shield_broken_counter == 2:
            shield_broken_counter = 0
            total_expenses += armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
