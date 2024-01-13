events = input().split("|")
total_coins = 100
total_energy = 100
for event in events:
    event_items = event.split("-")
    event_type = event_items[0]
    event_value = int(event_items[1])
    # Махаме тирето, като правим лист чрез split()
    # Типа 'събитие' се определя от първата (лява) част,
    # а 'стойността' от втората (дясната), със съответни индекси 0 и 1
    if event_type == 'rest':
        current_energy = total_energy   # Помощна променлива
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif event_type == 'order':
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print(f"You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
