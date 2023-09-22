daily_target = int(input())
earned = 0

input_line = input()
while input_line != 'closed':
    service = input_line
    income = 0

    if service == 'haircut':
        client = input()
        if client == 'mens':
            income += 15
        elif client == 'ladies':
            income += 20
        elif client == 'kids':
            income += 10

    elif service == 'color':
        type_coloring = input()
        if type_coloring == 'touch up':
            income += 20
        elif type_coloring == 'full color':
            income += 30

    earned += income

    if earned >= daily_target: break

    input_line = input()

diff = abs(earned - daily_target)
if earned >= daily_target:
    print(f"You have reached your target for the day!")
    print(f"Earned money: {earned}lv.")
else:
    print(f"Target not reached! You need {diff}lv. more.")
    print(f"Earned money: {earned}lv.")
