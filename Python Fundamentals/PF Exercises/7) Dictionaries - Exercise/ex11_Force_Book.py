force_book = {}

command = input()
while command != 'Lumpawaroo':

    if '|' in command:
        user_in_the_book = False
        force_side, force_user = command.split(" | ")
        for value in force_book.values():
            if force_user in value:
                user_in_the_book = True
                break
        if not user_in_the_book:
            if force_side not in force_book.keys():
                force_book[force_side] = []
            force_book[force_side].append(force_user)

    elif '->' in command:
        force_user, force_side = command.split(" -> ")
        for value in force_book.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in force_book.keys():
            force_book[force_side] = []
        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for force, users in force_book.items():
    members = len(users)
    if members > 0:
        print(f"Side: {force}, Members: {members}")
        for user in users:
            print(f"! {user}")
