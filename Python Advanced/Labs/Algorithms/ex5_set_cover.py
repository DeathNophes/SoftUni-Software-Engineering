def set_cover(universe, sets):
    chosen_sets = []

    while universe:
        best_set = max(sets, key=lambda s: len(universe.intersection(s)))
        # The set that covers the most elements from the universe
        chosen_sets.append(best_set)
        universe -= best_set

    return chosen_sets


universe_set = {int(x) for x in input().split(', ')}
sets_count = int(input())
sets_list = [{int(x) for x in input().split(', ')} for _ in range(sets_count)]

result = set_cover(universe_set, sets_list)

for i in range(len(result)):        # We change the items in the list
    result[i] = sorted(result[i])

print(f"Sets to take ({len(result)}):")
[print("{ " + f"{', '.join(str(x) for x in s)}" + " }") for s in result]
