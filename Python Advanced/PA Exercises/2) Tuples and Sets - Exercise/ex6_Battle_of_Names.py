n = int(input())
odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name = input()
    name_value = sum(ord(char) for char in name) // i
    if name_value % 2 == 0:
        even_set.add(name_value)
    else:
        odd_set.add(name_value)

if sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)

print(*result, sep=', ')
