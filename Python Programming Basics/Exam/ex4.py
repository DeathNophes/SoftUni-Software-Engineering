from math import ceil

workout_days = int(input())
first_days_km = float(input())

sum_km = first_days_km

previous_day = first_days_km
for _ in range(1, workout_days + 1):
    increment_percent = int(input())
    today_km = previous_day * (1 + (increment_percent / 100))
    sum_km += today_km

    previous_day = today_km

diff = abs(1000 - sum_km)
if sum_km >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")