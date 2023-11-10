inventory = {"shards": 0,
             "fragments": 0,
             "motes": 0,
             "junk": {}
             }
# We make our dictionary

item_found = False # flag
while True:
    if item_found:
        break
    data = input().split()
    # Judge will give us multiple rows of entry, so we need to put it in for-loops

    for i in range(0, len(data), 2):
        quantity, item = data[i], data[i + 1]
        quantity = int(quantity)
        item = item.lower()

        if item in inventory.keys():
            inventory[item] += quantity
            if inventory[item] >= 250:
                item_found = True

                if inventory['shards'] >= 250:
                    print("Shadowmourne obtained!")
                    inventory[item] -= 250
                    break

                elif inventory['fragments'] >= 250:
                    print("Valanyr obtained!")
                    inventory[item] -= 250
                    break

                elif inventory['motes'] >= 250:
                    print("Dragonwrath obtained!")
                    inventory[item] -= 250
                    break

        else:
            if item not in inventory["junk"]:
                inventory["junk"][item] = quantity
            else:
                inventory["junk"][item] += quantity

print(f"shards: {inventory['shards']}")
print(f"fragments: {inventory['fragments']}")
print(f"motes: {inventory['motes']}")
for key, value in inventory['junk'].items():
    print(f"{key}: {value}")
