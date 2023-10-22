targets = [int(digit) for digit in input().split()]
shot_targets = 0

command = input()
while command != "End":
    given_index = int(command)

    if 0 <= given_index < len(targets) and targets[given_index] != -1:
        target_value = targets[given_index]
        targets[given_index] = -1

        for i in range(len(targets)):
            if targets[i] == -1:
                continue
            elif targets[i] <= target_value:
                targets[i] += target_value
            elif targets[i] > target_value:
                targets[i] -= target_value

        shot_targets += 1

    command = input()

print(f"Shot targets: {shot_targets} -> ", end="")
for number in targets:
    print(number, end=" ")
