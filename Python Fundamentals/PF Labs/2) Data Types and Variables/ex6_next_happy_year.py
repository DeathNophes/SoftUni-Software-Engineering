year = int(input())
special_year = False

while not special_year:
    year += 1
    year_as_string = str(year)
    special_year = True
    for digit in year_as_string:
        if year_as_string.count(digit) > 1:
            special_year = False
            break
print(year)
