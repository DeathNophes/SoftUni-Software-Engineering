import re

items = input()
pattern = r'([#|]{1})([\sA-Za-z]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'
calories_per_day = 2000

my_calories = 0
foods = re.finditer(pattern, items)
for food in foods:
    my_calories += int(food.group(4))
days = my_calories // calories_per_day
print(f"You have food to last you for: {days} days!")

list_foods = re.finditer(pattern, items)
for current_food in list_foods:
    item = current_food.group(2)
    expiration_date = current_food.group(3)
    calories = current_food.group(4)
    print(f"Item: {item}, Best before: {expiration_date}, Nutrition: {calories}")
