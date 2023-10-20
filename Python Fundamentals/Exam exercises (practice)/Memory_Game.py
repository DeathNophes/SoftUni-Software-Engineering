def is_invalid(index_1, index_2):
    if index_1 == index_2:
        return True
    elif index_1 < 0 or index_1 > len(sequence_of_elements) - 1:
        return True
    elif index_2 < 0 or index_2 > len(sequence_of_elements) - 1:
        return True
    return False


def who_is_bigger(index_1, index_2):
    if index_1 > index_2:
        return index_1, index_2
    return index_2, index_1


sequence_of_elements = input().split()
input_line = input()
current_turn = 1

while input_line != 'end':
    data = list(map(int, input_line.split()))
    index1, index2 = data[0], data[1]

    if not sequence_of_elements:
        input_line = input()
        continue

    elif is_invalid(index1, index2):
        middle_index = len(sequence_of_elements) // 2
        sequence_of_elements.insert(middle_index, f"-{current_turn}a")
        sequence_of_elements.insert(middle_index, f"-{current_turn}a")
        print("Invalid input! Adding additional elements to the board")

    elif sequence_of_elements[index1] == sequence_of_elements[index2]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[index1]}!")
        bigger_index, smaller_index = who_is_bigger(index1, index2)
        sequence_of_elements.pop(bigger_index)
        sequence_of_elements.pop(smaller_index)

    elif sequence_of_elements[index1] != sequence_of_elements[index2]:
        print("Try again!")

    if sequence_of_elements:
        current_turn += 1
    input_line = input()
else:
    if sequence_of_elements:
        print(f"Sorry you lose :(")
        for symbol in sequence_of_elements:
            if symbol.isdigit():
                print(int(symbol), end=" ")
            else:
                print(symbol, end=" ")
    else:
        print(f"You have won in {current_turn} turns!")
