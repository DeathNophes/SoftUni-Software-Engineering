def exchange(some_numbers: list):
    exchanged_part = index_exchanger + 1
    left_part = some_numbers[0:exchanged_part]
    right_part = some_numbers[exchanged_part:]
    return right_part + left_part


def max_even():
    if not all_evens:
        return "No matches"
    max_even_number = max(all_evens)
    max_number_count = initial_line_int.count(max_even_number)
    current_max_count = 0
    for index in range(len(initial_line_int)):
        if initial_line_int[index] == max_even_number:
            current_max_count += 1
        if max_number_count == current_max_count:
            return index


def max_odd():
    if not all_odds:
        return "No matches"
    max_odd_number = max(all_odds)
    max_odd_count = initial_line_int.count(max_odd_number)
    current_max_count = 0
    for index in range(len(initial_line_int)):
        if initial_line_int[index] == max_odd_number:
            current_max_count += 1
        if max_odd_count == current_max_count:
            return index


def min_even():
    if not all_evens:
        return "No matches"
    min_even_number = min(all_evens)
    min_odd_count = initial_line_int.count(min_even_number)
    current_min_count = 0
    for index in range(len(initial_line_int)):
        if initial_line_int[index] == min_even_number:
            current_min_count += 1
        if min_odd_count == current_min_count:
            return index


def min_odd():
    if not all_odds:
        return "No matches"
    min_odd_number = min(all_odds)
    min_odd_count = initial_line_int.count(min_odd_number)
    current_min_count = 0
    for index in range(len(initial_line_int)):
        if initial_line_int[index] == min_odd_number:
            current_min_count += 1
        if min_odd_count == current_min_count:
            return index


def first_even(some_counter: int):
    if not all_evens:
        return "[]"
    my_even_list = []
    if some_counter > len(all_evens):
        some_counter = len(all_evens)
    for index in range(some_counter):
        my_even_list.append(all_evens[index])
    return my_even_list


def first_odd(some_counter: int):
    if not all_odds:
        return "[]"
    my_odd_list = []
    if some_counter > len(all_odds):
        some_counter = len(all_odds)
    for index in range(some_counter):
        my_odd_list.append(all_odds[index])
    return my_odd_list


def last_even(some_counter: int):
    if not all_evens:
        return "[]"
    if some_counter > len(all_evens):
        some_counter = len(all_evens)
    exchanger = len(all_evens) - some_counter
    return all_evens[exchanger:]


def last_odd(some_counter: int):
    if not all_odds:
        return "[]"
    if some_counter > len(all_odds):
        some_counter = len(all_odds)
    exchanger = len(all_odds) - some_counter
    return all_odds[exchanger:]


initial_line = input().split()
initial_line_int = [int(num) for num in initial_line]   # Str -> Int

input_line = input()
while input_line != 'end':
    command = input_line.split()
    all_evens = [num for num in initial_line_int if num % 2 == 0]
    all_odds = [num for num in initial_line_int if num % 2 == 1]

    if "exchange" in command:
        index_exchanger = int(command[1])
        if index_exchanger >= len(initial_line_int) or index_exchanger < 0:
            print("Invalid index")
        else:
            initial_line_int = exchange(initial_line_int)     # initial_line_int becomes something new

    elif "max" in command:
        if 'even' in command:
            print(max_even())
        elif 'odd' in command:
            print(max_odd())

    elif "min" in command:
        if 'even' in command:
            print(min_even())
        elif 'odd' in command:
            print(min_odd())

    elif "first" in command:
        counter = int(command[1])
        if counter > len(initial_line_int):
            print("Invalid count")
        elif 'even' in command:
            print(first_even(counter))
        elif 'odd' in command:
            print(first_odd(counter))

    elif "last" in command:
        counter = int(command[1])
        if counter > len(initial_line_int):
            print("Invalid count")
        elif 'even' in command:
            print(last_even(counter))
        elif 'odd' in command:
            print(last_odd(counter))

    input_line = input()

print(initial_line_int)
