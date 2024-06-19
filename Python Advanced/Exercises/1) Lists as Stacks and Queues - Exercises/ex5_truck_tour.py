from collections import deque

petrol_stations = deque()
n = int(input())

for _ in range(n):
    petrol_stations.append(input().split())

petrol_stations_clone = petrol_stations.copy()

success_count = 0
while success_count != len(petrol_stations):
    current_fuel = 0
    for station in petrol_stations_clone:
        refill_petrol = int(station[0])
        distance_to_next_station = int(station[1])
        current_fuel += refill_petrol
        if distance_to_next_station > current_fuel:
            petrol_stations_clone.rotate(-1)
            success_count = 0
            break
        else:
            success_count += 1
            current_fuel -= distance_to_next_station

index = petrol_stations.index(petrol_stations_clone[0])
print(index)
