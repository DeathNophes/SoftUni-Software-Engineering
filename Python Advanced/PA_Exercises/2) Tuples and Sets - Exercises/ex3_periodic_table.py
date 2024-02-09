n = int(input())
unique_chemicals = set()
for _ in range(n):
    chemicals = input().split()
    for chemical in chemicals:
        unique_chemicals.add(chemical)

for chemical in unique_chemicals:
    print(chemical)