gifts_list = input().split(" ")
command = input()

while command != 'No Money':
    command = command.split(" ")

    if "OutOfStock" in command:
        for i in range(len(gifts_list)):
            if gifts_list[i] == command[1]:
                gifts_list[i] = 'None'

    elif "Required" in command:
        for i in range(len(gifts_list)):
            if i == int(command[2]):
                gifts_list[i] = command[1]

    elif "JustInCase" in command:
        gifts_list[-1] = command[1]

    command = input()

while "None" in gifts_list:
    gifts_list.remove("None")

print(*gifts_list, sep=" ")
