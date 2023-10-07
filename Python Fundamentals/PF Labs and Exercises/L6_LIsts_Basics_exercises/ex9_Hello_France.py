items_list = input().split("|")
budget = float(input())
bought_items_prices = []
new_prices = []
profit = 0
total_money = 0

for item in items_list:
    current_item = item.split("->")
    name = current_item[0]
    price = float(current_item[1])
    if name == "Clothes" and price <= 50.00:
        if budget < price:
            continue
        budget -= price
        bought_items_prices.append(price)

    elif name == "Shoes" and price <= 35.00:
        if budget < price:
            continue
        budget -= price
        bought_items_prices.append(price)

    elif name == "Accessories" and price <= 20.50:
        if budget < price:
            continue
        budget -= price
        bought_items_prices.append(price)

for old_price in bought_items_prices:
    current_price = old_price
    new_price = old_price * 1.4
    profit += (new_price - current_price)
    new_prices.append(new_price)
    total_money += new_price

formatted_new_prices = list(map(lambda n: "%.2f" % n, new_prices))
total_money += budget

print(*formatted_new_prices, sep=" ")
print(f"Profit: {profit:.2f}")
if total_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
