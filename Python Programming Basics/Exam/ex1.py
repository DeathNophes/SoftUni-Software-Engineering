paper_rolls = int(input())
cloth_rolls = int(input())
glue_lt = float(input())
percent_discount = int(input())

paper_price = paper_rolls * 5.80
cloth_price = cloth_rolls * 7.20
glue_price = glue_lt * 1.20

material_price = paper_price + cloth_price + glue_price

total_price = material_price * (1 - (percent_discount / 100))
print(f"{total_price:.3f}")
