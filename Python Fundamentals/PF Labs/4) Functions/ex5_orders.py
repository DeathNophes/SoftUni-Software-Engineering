def order(product, quantity):
    if product == "coffee":
        return quantity * 1.50
    elif product == "coke":
        return quantity * 1.40
    elif product == "water":
        return quantity * 1.00
    elif product == "snacks":
        return quantity * 2.00


item = input()
amount = int(input())
result = order(item, amount)
print(f"{result:.2f}")
