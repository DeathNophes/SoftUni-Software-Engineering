stock = {}

line = input()
while line != 'statistics':
    product, quantity = line.split(":")
    quantity = int(quantity)
    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity
    line = input()

product_count = len(stock.keys())
total_quantity = sum(stock.values())

print('Products in stock: ')
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {product_count}")
print(f"Total Quantity: {total_quantity}")
