numbers = tuple(float(el) for el in input().split())
occ = {}
for num in numbers:
    if num not in occ.keys():
        number_count = numbers.count(num)
        occ[num] = number_count
        print(f"{num} - {number_count} times")
