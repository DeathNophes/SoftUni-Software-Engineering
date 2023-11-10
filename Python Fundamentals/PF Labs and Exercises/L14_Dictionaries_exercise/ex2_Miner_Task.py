resources = {}

while True:
    curr_resource = input()
    if curr_resource == 'stop':
        break
    quantity = int(input())

    if curr_resource not in resources.keys():
        resources[curr_resource] = 0
    resources[curr_resource] += quantity

for resource, amount in resources.items():
    print(f"{resource} -> {amount}")
