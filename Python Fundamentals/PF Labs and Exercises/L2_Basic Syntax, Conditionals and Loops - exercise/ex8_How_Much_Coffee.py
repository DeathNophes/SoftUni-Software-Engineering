coffee_counter = 0
command = input()
while command != 'END':
    if command.lower() == 'coding' \
            or command.lower() == 'dog' \
            or command.lower() == 'cat' \
            or command.lower() == 'movie':
        # lower() я използваме, за да превръщаме в дума с малки букви,
        # а тук с нея също гледаме дали думата е от правилните
        if command.islower(): # Дали е с малки букви - True / False
            coffee_counter += 1
        else: # Дали е с големи букви True / False
            coffee_counter += 2
    command = input()

if coffee_counter > 5:
    print('You need extra sleep')
else:
    print(coffee_counter)
