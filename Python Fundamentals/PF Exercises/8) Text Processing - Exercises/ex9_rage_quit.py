text = input()
rage_quit = ''
curr_symbols = ''
repetitions = ''
for index in range(len(text)):
    if not text[index].isdigit():    # the symbol in non-numerical
        curr_symbols += text[index].upper()
    else:    # We have a digit --> time for repetitions
        for next_symbol in range(index, len(text)):
            if not text[next_symbol].isdigit():
                break
            repetitions += text[next_symbol]
        rage_quit += curr_symbols * int(repetitions)
        curr_symbols = ''
        repetitions = ''
print(f"Unique symbols used: {len(set(rage_quit))}")
print(rage_quit)
