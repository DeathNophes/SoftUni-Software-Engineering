import re

total_value = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"

print('Bought furniture:')
line = input()
while line != 'Purchase':
    match = re.match(pattern, line)
    if match:
        furniture, price, quantity = match.groups()
        # We have exactly 3 groups
        print(furniture)
        total_value += int(quantity) * float(price)
    line = input()
print(f"Total money spend: {total_value:.2f}")
