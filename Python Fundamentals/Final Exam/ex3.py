guestbook = {}
unliked_meals = 0

command = input()
while command != 'Stop':
    command = command.split('-')
    guest, meal = command[1], command[2]

    if 'Like' in command:
        if guest not in guestbook.keys():
            guestbook[guest] = []
            guestbook[guest].append(meal)
        else:
            if meal not in guestbook[guest]:
                guestbook[guest].append(meal)

    elif 'Dislike' in command:
        if guest not in guestbook.keys():
            print(f'{guest} is not at the party.')

        elif meal not in guestbook[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")

        else:
            guestbook[guest].remove(meal)
            print(f"{guest} doesn't like the {meal}.")
            unliked_meals += 1

    command = input()

for current_guest, meals in guestbook.items():
    print(f"{current_guest}: {', '.join(meals)}")
print(f"Unliked meals: {unliked_meals}")