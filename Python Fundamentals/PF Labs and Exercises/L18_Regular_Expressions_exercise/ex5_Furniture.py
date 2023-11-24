import re

total_value = 0
pattern = r"^>>([A-Za-z]+)<<(\d+[.]{0,1}\d+)*!(\d+\b)"

print('Bought furniture:')
line = input()
while line != 'Purchase':
    result = re.match(pattern, line)
    if result:
        print(result.group(1))
        price = float(result.group(2))
        quantity = int(result.group(3))
        total_value += (quantity * price)
    line = input()
print(f"Total money spend: {total_value:.2f}")
