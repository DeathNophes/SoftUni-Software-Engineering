budget = int(input())

input_line = input()
while input_line != 'End':
    current_price = int(input_line)
    budget -= current_price

    if budget < 0:
        print(f"You went in overdraft!")
        break

    input_line = input()
else:
    print("You bought everything needed.")