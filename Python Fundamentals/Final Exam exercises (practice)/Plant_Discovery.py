n = int(input())
plants_book = {}

for _ in range(n):
    current_plant = input().split('<->')
    plant, rarity = current_plant[0], current_plant[1]
    if plant not in plants_book.keys():
        plants_book[plant] = {'Rarity': rarity, 'Rating': 0, 'R_count': 0}
    else:
        plants_book[plant]['Rarity'] = rarity

command = input()
while command != 'Exhibition':
    command = command.split()
    plant = command[1]
    if plant not in plants_book.keys():
        print('error')

    elif 'Rate:' in command:
        rating = float(command[3])
        plants_book[plant]['Rating'] += rating
        plants_book[plant]['R_count'] += 1

    elif 'Update:' in command:
        new_rarity = command[3]
        plants_book[plant]['Rarity'] = new_rarity

    elif 'Reset:' in command:
        plants_book[plant]['Rating'] = 0
        plants_book[plant]['R_count'] = 0

    command = input()

print('Plants for the exhibition:')
for plant in plants_book.keys():
    rarity = plants_book[plant]['Rarity']
    current_rating = plants_book[plant]['Rating']
    current_rating_counter = plants_book[plant]['R_count']
    if current_rating == 0 or current_rating_counter == 0:
        avg_rating = 0
    else:
        avg_rating = current_rating / current_rating_counter
    print(f"- {plant}; Rarity: {rarity}; Rating: {avg_rating:.2f}")
