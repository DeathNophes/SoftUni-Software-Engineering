n, m = [int(x) for x in input().split()]
first_set = set()
second_set = set()

for _ in range(n):
    num = input()
    first_set.add(num)
for _ in range(m):
    num = input()
    second_set.add(num)

new_set = first_set & second_set
# Intersection
for number in new_set:
    print(number)
