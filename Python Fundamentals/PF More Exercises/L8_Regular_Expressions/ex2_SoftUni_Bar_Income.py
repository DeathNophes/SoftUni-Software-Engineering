import re

pattern = r"%(?P<customer>[A-Z][a-z]+)%[^|$%.]*?<(?P<product>\w+)>[^|$%.]*?\|(?P<count>\d+)\|[^|$%.]*?" \
          r"(?P<price>[0-9]+(\.[0-9]+)?)\$"

total_income = 0

line = input()
while line != "end of shift":
    data = re.search(pattern, line)
    if data:
        customer = data.group('customer')
        product = data.group('product')
        price = float(data.group('price').replace('$', "")) * int(data.group('count'))
        print(f"{customer}: {product} - {price:.2f}")
        total_income += price
    line = input()
print(f"Total income: {total_income:.2f}")