def where_is_wolf(some_animals: list) -> str:
    if some_animals[-1] == 'wolf':
        return "Please go away and stop eating my sheep"
    sheep_count = 0
    for i in reversed(animals):
        if i == 'wolf':
            return f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!"
        sheep_count += 1


animals = input().split(", ")
print(where_is_wolf(animals))
