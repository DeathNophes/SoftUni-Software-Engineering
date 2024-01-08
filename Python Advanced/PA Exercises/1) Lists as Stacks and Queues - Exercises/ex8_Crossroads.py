from collections import deque

green_light = int(input())
free_window = int(input())
crossed_cars_count = 0
cars_queue = deque()

command = input()
while command != 'END':
    if command == 'green':
        if cars_queue:
            current_car = cars_queue.popleft()
            seconds_left = green_light - len(current_car)
            while seconds_left > 0:
                crossed_cars_count += 1
                if cars_queue:
                    current_car = cars_queue.popleft()
                    seconds_left -= len(current_car)
                else:
                    break
            if seconds_left == 0:
                crossed_cars_count += 1
            if free_window >= abs(seconds_left):
                if seconds_left < 0:
                    crossed_cars_count += 1
            else:
                index = free_window + seconds_left
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[index]}.")
                exit()
    else:
        cars_queue.append(command)
    command = input()

print("Everyone is safe.")
print(f"{crossed_cars_count} total cars passed the crossroads.")