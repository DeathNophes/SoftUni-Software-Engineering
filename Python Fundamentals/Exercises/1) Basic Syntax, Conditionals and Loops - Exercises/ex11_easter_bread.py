budget = float(input())
one_kg_flour_price = float(input())

amount_left = budget
one_pack_eggs_price = one_kg_flour_price * 0.75
one_lt_milk_price = one_kg_flour_price * 1.25
loaf_counter = 0
eggs_counter = 0

while True:
    current_loaf_price = one_pack_eggs_price + one_kg_flour_price + (one_lt_milk_price * 0.25)
    if amount_left - current_loaf_price <= 0:
        break
    amount_left -= current_loaf_price
    loaf_counter += 1
    eggs_counter += 3
    if loaf_counter % 3 == 0:
        eggs_counter -= (loaf_counter - 2)

print(f"You made {loaf_counter} loaves of Easter bread!"
      f" Now you have {eggs_counter} eggs and {amount_left:.2f}BGN left.")
