vehicles = input().split(">>")
all_taxes = 0

for current_vehicle in range(len(vehicles)):
    this_vehicle = vehicles[current_vehicle].split()
    current_vehicle_tax = 0
    years_for_tax = int(this_vehicle[1])
    kilometers = int(this_vehicle[2])

    if "family" in this_vehicle:
        initial_tax = 50
        initial_tax -= (5 * years_for_tax)
        traveled_3k_count = kilometers // 3000
        initial_tax += traveled_3k_count * 12
        current_vehicle_tax += initial_tax
        print(f"A family car will pay {current_vehicle_tax:.2f} euros in taxes.")

    elif "heavyDuty" in this_vehicle:
        initial_tax = 80
        initial_tax -= (8 * years_for_tax)
        traveled_9k_count = kilometers // 9000
        initial_tax += traveled_9k_count * 14
        current_vehicle_tax += initial_tax
        print(f"A heavyDuty car will pay {current_vehicle_tax:.2f} euros in taxes.")

    elif "sports" in this_vehicle:
        initial_tax = 100
        initial_tax -= (9 * years_for_tax)
        traveled_2k_count = kilometers // 2000
        initial_tax += traveled_2k_count * 18
        current_vehicle_tax += initial_tax
        print(f"A sports car will pay {current_vehicle_tax:.2f} euros in taxes.")

    else:
        print("Invalid car type.")

    all_taxes += current_vehicle_tax

print(f"The National Revenue Agency will collect {all_taxes:.2f} euros in taxes.")
