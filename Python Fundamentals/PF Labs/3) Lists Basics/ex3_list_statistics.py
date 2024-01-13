n = int(input())
positive_zero_list = []
negative_list = []

for _ in range(n):
    number = int(input())
    if number >= 0:
        positive_zero_list.append(number)
    else:
        negative_list.append(number)

print(positive_zero_list)
print(negative_list)
print(f"Count of positives: {len(positive_zero_list)}")
print(f"Sum of negatives: {sum(negative_list)}")
