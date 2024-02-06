from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumption_index = deque(int(x) for x in input().split())
altitudes_distance = deque(int(x) for x in input().split())

reached_altitudes = []

curr_altitude = 0
while altitudes_distance:
    if (initial_fuel[-1] - consumption_index[0]) >= altitudes_distance[0]:
        curr_altitude += 1
        print(f"John has reached: Altitude {curr_altitude}")
        reached_altitudes.append(f"Altitude {curr_altitude}")
        initial_fuel.pop()
        consumption_index.popleft()
        altitudes_distance.popleft()

    else:
        print(f"John did not reach: Altitude {curr_altitude + 1}")
        break

else:
    print("John has reached all the altitudes and managed to reach the top!")
    exit()

if curr_altitude == 0:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
else:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '. join(reached_altitudes)}")

