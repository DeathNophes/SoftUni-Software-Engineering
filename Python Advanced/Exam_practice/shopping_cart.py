def shopping_cart(*args):
    result = ""

    max_products = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2
    }

    my_meals = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }

    for element in args:
        if element == 'Stop':
            break

        meal, product = element

        if product not in my_meals[meal]:
            if len(my_meals[meal]) < max_products[meal]:
                my_meals[meal].append(product)

    my_sorted_meals = sorted(my_meals.items(), key=lambda x: (-len(x[1]), x[0]))

    for meal, products_list in my_sorted_meals:
        result += f"{meal}:\n"
        for product in sorted(products_list):
            result += f" - {product}\n"

    if not my_meals['Pizza'] and not my_meals['Soup'] and not my_meals['Dessert']:
        result = 'No products in the cart!'

    return result
