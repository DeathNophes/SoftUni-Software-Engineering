fires = input().split("#")
water = int(input())
total_fire = 0
total_effort = 0
print("Cells:")
for fire in fires:
    current_fire = fire.split()
    fire_type = current_fire[0]
    cell_value = int(current_fire[2])

    if fire_type == "High" and 81 <= cell_value <= 125:
        if water < cell_value:
            continue
        water -= cell_value
        total_effort += (0.25 * cell_value)
        total_fire += cell_value

    elif fire_type == "Medium" and 51 <= cell_value <= 80:
        if water < cell_value:
            continue
        water -= cell_value
        total_effort += (0.25 * cell_value)
        total_fire += cell_value

    elif fire_type == "Low" and 1 <= cell_value <= 50:
        if water < cell_value:
            continue
        water -= cell_value
        total_effort += (0.25 * cell_value)
        total_fire += cell_value
    else:
        continue

    print(f"- {cell_value}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
