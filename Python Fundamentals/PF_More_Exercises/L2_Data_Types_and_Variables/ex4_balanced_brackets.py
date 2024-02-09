n = int(input())
open_bracket_counter = 0
closed_bracket_counter = 0
for i in range(n):
    symbol = input()
    if symbol == "(":
        open_bracket_counter += 1
    if symbol == ")":
        closed_bracket_counter += 1
        if open_bracket_counter == 0:
            print("UNBALANCED")
            break
    if open_bracket_counter > 1 or closed_bracket_counter > 1:
        print("UNBALANCED")
        break
    if open_bracket_counter == 1 and closed_bracket_counter == 1:
        open_bracket_counter = 0
        closed_bracket_counter = 0
else:
    print("BALANCED")
