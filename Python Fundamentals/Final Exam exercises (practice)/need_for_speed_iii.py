n = int(input())
cars = {}
for _ in range(n):
    current_car = input().split('|')
    car = current_car[0]
    mileage = int(current_car[1])
    fuel = int(current_car[2])
    cars[car] = {'mileage': mileage, 'fuel': fuel}

command = input()
while command != 'Stop':
    command = command.split(' : ')
    car = command[1]
    if 'Drive' in command:
        distance = int(command[2])
        fuel = int(command[3])
        if cars[car]['fuel'] >= fuel:
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]['mileage'] >= 100000:
                print(f"Time to sell the {car}!")
                del cars[car]
        else:
            print("Not enough fuel to make that ride")

    elif 'Refuel' in command:
        fuel = int(command[2])
        if cars[car]['fuel'] + fuel > 75:
            diff = 75 - cars[car]['fuel']
            cars[car]['fuel'] += diff
            print(f"{car} refueled with {diff} liters")
        else:
            cars[car]['fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif 'Revert' in command:
        kilometers = int(command[2])
        if cars[car]['mileage'] - kilometers >= 10000:
            cars[car]['mileage'] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars[car]['mileage'] = 10000

    command = input()

for curr_car in cars.keys():
    curr_fuel = cars[curr_car]['fuel']
    curr_mileage = cars[curr_car]['mileage']
    print(f"{curr_car} -> Mileage: {curr_mileage} kms, Fuel in the tank: {curr_fuel} lt.")
