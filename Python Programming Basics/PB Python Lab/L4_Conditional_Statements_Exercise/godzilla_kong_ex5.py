budget = float(input())
statist_count = int(input())
clothes_price = float(input())

decoration = budget * 0.10
# Декорацията е 10% от Бюджета
sum_clothes = statist_count * clothes_price

if statist_count > 150:
    sum_clothes = sum_clothes * 0.90
# 10% отстъпка при повече от 150 статиста
total_sum = sum_clothes + decoration

diff = abs(budget - total_sum)
# Използваме абсолютна стойност
if budget >= total_sum:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")