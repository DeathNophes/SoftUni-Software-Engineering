from collections import deque

programmers_time = deque([int(x) for x in input().split()])
task_complexities = [int(x) for x in input().split()]

my_ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while programmers_time and task_complexities:
    curr_time = programmers_time[0]
    curr_task_time = task_complexities[-1]
    result = curr_time * curr_task_time

    if 0 <= result <= 60:
        my_ducks["Darth Vader Ducky"] += 1

    elif 61 <= result <= 120:
        my_ducks["Thor Ducky"] += 1

    elif 121 <= result <= 180:
        my_ducks["Big Blue Rubber Ducky"] += 1

    elif 181 <= result <= 240:
        my_ducks["Small Yellow Rubber Ducky"] += 1

    else:
        task_complexities[-1] -= 2
        programmers_time.rotate(-1)
        continue

    programmers_time.popleft()
    task_complexities.pop()

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for duck, quantity in my_ducks.items():
    print(f"{duck}: {quantity}")