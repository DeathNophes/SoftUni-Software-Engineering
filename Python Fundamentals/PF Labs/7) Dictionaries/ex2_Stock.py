products_information = input().split()

stock_data = {}

for i in range(0, len(products_information), 2):
    product = products_information[i]
    quantity = int(products_information[i + 1])
    stock_data[product] = quantity

searched_products = input().split()

for product in searched_products:
    if product in stock_data.keys():
        curr_quantity = stock_data[product]
        print(f"We have {curr_quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
