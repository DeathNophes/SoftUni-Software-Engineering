energy = int(input())

battles_won = 0
command = input()
while command != "End of battle":
    distance = int(command)

    if energy - distance >= 0:
        battles_won += 1
        energy -= distance
        if battles_won % 3 == 0:
            energy += battles_won
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
        break

    command = input()

else:
    print(f"Won battles: {battles_won}. Energy left: {energy}")
