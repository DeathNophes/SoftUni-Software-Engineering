number_of_pieces = int(input())
music_dict = {}
for _ in range(number_of_pieces):
    this_piece, composer, key = input().split('|')
    music_dict[this_piece] = [composer, key]

command = input()
while command != 'Stop':
    command = command.split('|')
    if 'Add' in command:
        current_piece, composer, key = command[1], command[2], command[3]
        if current_piece not in music_dict.keys():
            music_dict[current_piece] = [composer, key]
            print(f"{current_piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{current_piece} is already in the collection!")

    elif 'Remove' in command:
        current_piece = command[1]
        if current_piece in music_dict.keys():
            music_dict.pop(current_piece)
            print(f"Successfully removed {current_piece}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")

    elif 'ChangeKey' in command:
        current_piece, new_key = command[1], command[2]
        if current_piece in music_dict.keys():
            music_dict[current_piece][1] = new_key
            print(f"Changed the key of {current_piece} to {new_key}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")

    command = input()

for curr_piece in music_dict.keys():
    current_composer = music_dict[curr_piece][0]
    current_key = music_dict[curr_piece][1]
    print(f"{curr_piece} -> Composer: {current_composer}, Key: {current_key}")
