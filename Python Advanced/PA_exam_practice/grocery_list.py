def shop_from_grocery_list(budget, buying_list, *args):
    result = ""

    for item, price in args:
        if budget < price:
            break

        if item in buying_list:
            budget -= price
            buying_list.remove(item)

    if not buying_list:
        result += f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        result += f"You did not buy all the products. Missing products: {', '.join(buying_list)}."

    return result
