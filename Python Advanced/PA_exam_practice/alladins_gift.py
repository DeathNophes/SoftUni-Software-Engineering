from collections import deque


def add_an_item(calculation):
    if 100 <= calculation <= 199:
        my_items["Gemstone"] += 1

    elif 200 <= calculation <= 299:
        my_items["Porcelain Sculpture"] += 1

    elif 300 <= calculation <= 399:
        my_items["Gold"] += 1

    elif 400 <= calculation <= 499:
        my_items["Diamond Jewellery"] += 1


def are_we_ready():
    if my_items["Gemstone"] > 0 and my_items["Porcelain Sculpture"] > 0:
        return True
    elif my_items["Gold"] > 0 and my_items["Diamond Jewellery"] > 0:
        return True
    return False


my_items = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

materials = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])

while materials and magic_values:
    result = materials[-1] + magic_values[0]

    if 100 <= result <= 499:
        add_an_item(result)

    elif result < 100:
        if result % 2 == 0:
            materials[-1] *= 2
            magic_values[0] *= 3
            result = materials[-1] + magic_values[0]
            add_an_item(result)
        else:
            result *= 2
            add_an_item(result)

    elif result > 499:
        result /= 2
        add_an_item(result)

    materials.pop()
    magic_values.popleft()


if are_we_ready():
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

for item, quantity in sorted(my_items.items(), key=lambda x: x[0]):
    if quantity:
        print(f"{item}: {quantity}")