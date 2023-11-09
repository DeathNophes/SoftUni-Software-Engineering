neighbourhood = list(map(int, input().split("@")))
current_position = 0

command = input()
while command != "Love!":
    action = command.split()
    length = int(action[1])

    if current_position + length >= len(neighbourhood):
        current_position = 0
    else:
        current_position += length

    if neighbourhood[current_position] == 0:
        print(f"Place {current_position} already had Valentine's day.")

    elif neighbourhood[current_position] > 0:
        neighbourhood[current_position] -= 2
        if neighbourhood[current_position] == 0:
            print(f"Place {current_position} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {current_position}.")
if sum(neighbourhood) == 0:
    print("Mission was successful.")
else:
    houses_without_valentine = [digit for digit in neighbourhood if digit > 0]
    print(f"Cupid has failed {len(houses_without_valentine)} places.")

