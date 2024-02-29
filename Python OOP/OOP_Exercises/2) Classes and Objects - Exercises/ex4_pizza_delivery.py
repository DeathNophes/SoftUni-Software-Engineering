class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict, ordered=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = ordered

    def get_ordered_message(self):
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return self.get_ordered_message()

        self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity

        self.price += (quantity * price_per_quantity)

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return self.get_ordered_message()

        ingredient_quantity = self.ingredients.get(ingredient)

        if not ingredient_quantity:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        elif quantity > ingredient_quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= (quantity * price_per_quantity)

    def make_order(self):
        self.ordered = True
        ingredients = ', '.join(f"{k}: {v}" for k, v in self.ingredients.items())
        return f"You've ordered pizza {self.name} prepared with {ingredients} " \
               f"and the price will be {self.price}lv."
