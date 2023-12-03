import re

items = input()
pattern = r'([#|]{1})([\sA-Za-z]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'
calories_per_day = 2000
foods = re.findall(pattern, items)
my_calories = sum(int(food[3]) for food in foods)
days = my_calories // 2000
print(f"You have food to last you for: {days} days!")
for food in foods:
    item = food[1]
    expiration_date = food[2]
    calories = food[3]
    print(f"Item: {item}, Best before: {expiration_date}, Nutrition: {calories}")
