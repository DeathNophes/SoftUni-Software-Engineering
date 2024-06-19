race_times_str = input().split()
race_times_int = []
for time in race_times_str:
    race_times_int.append(int(time))

middle = len(race_times_int) // 2
race_times_int.pop(middle)
left_racer = race_times_int[:middle]
right_racer = race_times_int[middle:]
left_racer_sum_minutes = 0
right_racer_sum_minutes = 0
for lap_min in left_racer:
    left_racer_sum_minutes += int(lap_min)
    if lap_min == 0:
        left_racer_sum_minutes *= 0.8
for lap_min in reversed(right_racer):
    right_racer_sum_minutes += int(lap_min)
    if lap_min == 0:
        right_racer_sum_minutes *= 0.8

if left_racer_sum_minutes < right_racer_sum_minutes:
    print(f"The winner is left with total time: {left_racer_sum_minutes:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_sum_minutes:.1f}")
