order = {}

while True:
    product = input()
    if product == 'buy':
        break
    name, price, quantity = product.split()
    price = float(price)
    quantity = int(quantity)

    if name not in order.keys():
        order[name] = {'price': price, 'quantity': quantity}
    else:
        order[name]['quantity'] += quantity
        if order[name]['price'] != price:
            order[name]['price'] = price
        # If the prices are different we add the quantity and change the price to the new one

for name in order.keys():
    curr_price = order[name]['price'] * order[name]['quantity']
    print(f"{name} -> {curr_price:.2f}")
