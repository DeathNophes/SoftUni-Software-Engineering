n = int(input())
current_water_in_the_tank = 0
tank_capacity = 255
for _ in range(n):
    current_liters = int(input())
    if current_water_in_the_tank + current_liters > tank_capacity:
        print("Insufficient capacity!")
        continue
    current_water_in_the_tank += current_liters
print(f"{current_water_in_the_tank}")
