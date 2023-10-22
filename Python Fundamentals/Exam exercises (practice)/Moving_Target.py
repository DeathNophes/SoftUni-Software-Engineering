targets = [int(digit) for digit in input().split()]

command = input()
while command != "End":
    data = command.split()

    if "Shoot" in command:
        index = int(data[1])
        power = int(data[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif "Add" in command:
        index = int(data[1])
        value = int(data[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif "Strike" in command:
        index = int(data[1])
        radius = int(data[2])
        if 0 <= index - radius and index + radius < len(targets):
            for i in range(index + radius, index - radius - 1, -1):
                targets.pop(i)
        else:
            print("Strike missed!")

    command = input()

new_list = [str(target) for target in targets]
print("|".join(new_list))