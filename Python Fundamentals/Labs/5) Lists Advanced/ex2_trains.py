wagons = [0] * int(input())    # Правим лист от чели числа (0)

while True:
    command = input().split()   # Разделяме командата на части от лист

    if 'End' in command:
        print(wagons)
        break
    elif 'add' in command:
        people = int(command[1])
        wagons[-1] += people
    elif 'insert' in command:
        index = int(command[1])
        people = int(command[2])
        wagons[index] += people
    elif 'leave' in command:
        index = int(command[1])
        people = int(command[2])
        wagons[index] -= people
