pirate_ship = [int(digit) for digit in input().split(">")]
warship = [int(digit) for digit in input().split(">")]
max_health_per_section = int(input())

input_line = input()
while input_line != "Retire":
    command = input_line.split()

    if "Fire" in command:
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                exit()

    elif "Defend" in command:
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif "Repair" in command:
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health_per_section:
                pirate_ship[index] = max_health_per_section

    elif "Status" in command:
        need_repair_soon = [section for section in pirate_ship if section < 0.20 * max_health_per_section]
        sections_for_repair_count = len(need_repair_soon)
        print(f"{sections_for_repair_count} sections need repair.")

    input_line = input()
else:
    print(f"Pirate ship status: {sum(pirate_ship)}\nWarship status: {sum(warship)}")
