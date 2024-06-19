def cookbook(*args):
    result = ""
    recipes = {}

    for element in args:
        recipe_name, cuisine, ingredients = element

        if cuisine not in recipes.keys():
            recipes[cuisine] = {}
        recipes[cuisine][recipe_name] = ingredients

    sorted_recipes = sorted(recipes.items(), key=lambda x: (-len(x[1]), x[0]))

    for element in sorted_recipes:
        cuisine_name, curr_recipes = element
        result += f"{cuisine_name} cuisine contains {len(curr_recipes)} recipes:\n"
        for recipe_name, ingredients in sorted(curr_recipes.items(), key=lambda x: x[0]):
            result += f"  * {recipe_name} -> Ingredients: {', '.join(ingredients)}\n"

    return result
