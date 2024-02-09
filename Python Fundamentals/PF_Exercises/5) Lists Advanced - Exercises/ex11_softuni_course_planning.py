schedule = input().split(", ")

input_line = input()
while input_line != "course start":
    command = input_line.split(":")

    if "Add" in command:
        title = command[1]
        if title not in schedule:
            schedule.append(title)

    elif "Insert" in command:
        title, index = command[1], int(command[2])
        if title not in schedule:
            schedule.insert(index, title)

    elif "Remove" in command:
        title = command[1]
        if title in schedule:
            schedule.remove(title)
        if f"{title}-Exercise" in schedule:
            schedule.remove(f"{title}-Exercise")

    elif "Swap" in command:
        title1, title2 = command[1], command[2]
        if title1 and title2 in schedule:
            title1_index = schedule.index(title1)
            title2_index = schedule.index(title2)
            schedule[title1_index], schedule[title2_index] = schedule[title2_index], schedule[title1_index]
            if f"{title1}-Exercise" in schedule and f"{title2}-Exercise" not in schedule:
                ex_index = schedule.index(f"{title1}-Exercise")
                schedule.insert(title2_index + 1, schedule.pop(ex_index))
            elif f"{title2}-Exercise" in schedule and f"{title1}-Exercise" not in schedule:
                ex_index = schedule.index(f"{title2}-Exercise")
                schedule.insert(title1_index + 1, schedule.pop(ex_index))
            elif f"{title1}-Exercise" in schedule and f"{title2}-Exercise" in schedule:
                title1_ex_index = schedule.index(f"{title1}-Exercise")
                title2_ex_index = schedule.index(f"{title2}-Exercise")
                title_1_ex = schedule.pop(title1_ex_index)
                title_2_ex = schedule.pop(title2_ex_index - 1)
                new_title1_index = schedule.index(title1)
                new_title2_index = schedule.index(title2)
                schedule.insert(new_title1_index + 1, title_1_ex)
                schedule.insert(new_title2_index + 1, title_2_ex)

    elif "Exercise" in command:
        title = command[1]
        if title in schedule and f"{title}-Exercise" not in schedule:
            title_index = schedule.index(title)
            schedule.insert(title_index + 1, f"{title}-Exercise")
        elif title not in schedule:
            schedule.append(title)
            schedule.append(f"{title}-Exercise")

    input_line = input()

counter = 1
for i in range(len(schedule)):
    print(f"{counter}.{schedule[i]}")
    counter += 1

