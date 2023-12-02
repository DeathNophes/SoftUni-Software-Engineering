current_map = {}

input_line = input()
while input_line != 'Sail':
    command = input_line.split('||')
    city = command[0]
    population = int(command[1])
    gold = int(command[2])

    if city not in current_map.keys():
        current_map[city] = {'population': population, 'gold': gold}
    else:
        current_map[city]['population'] += population
        current_map[city]['gold'] += gold

    input_line = input()


event = input()
while event != 'End':
    command = event.split('=>')
    town = command[1]

    if 'Plunder' in command:
        people_killed = int(command[2])
        gold_stolen = int(command[3])
        current_map[town]['population'] -= people_killed
        current_map[town]['gold'] -= gold_stolen
        print(f"{town} plundered! {gold_stolen} gold stolen, {people_killed} citizens killed.")
        if current_map[town]['population'] == 0 or current_map[town]['gold'] == 0:
            print(f"{town} has been wiped off the map!")
            del current_map[town]

    elif 'Prosper' in command:
        gold_gained = int(command[2])
        if gold_gained < 0:
            print(f"Gold added cannot be a negative number!")

        elif gold_gained > 0:
            current_map[town]['gold'] += gold_gained
            print(f"{gold_gained} gold added to the city treasury. {town} now has {current_map[town]['gold']} gold.")

    event = input()

if len(current_map) > 0:
    print(f"Ahoy, Captain! There are {len(current_map)} wealthy settlements to go to:")
    for town in current_map.keys():
        people = current_map[town]['population']
        gold = current_map[town]['gold']
        print(f"{town} -> Population: {people} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")