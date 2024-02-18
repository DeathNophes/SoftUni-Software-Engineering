def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    result = ""
    products_count = 0
    bought_products = {}

    for product_name, attributes in kwargs.items():
        price, quantity = attributes

        if budget > (price * quantity):
            products_count += 1
            bought_products[product_name] = (price * quantity)
            budget -= (price * quantity)

            if products_count == 5:
                break

    for name, price in bought_products.items():
        result += f"You bought {name} for {price:.2f} leva.\n"

    return result
