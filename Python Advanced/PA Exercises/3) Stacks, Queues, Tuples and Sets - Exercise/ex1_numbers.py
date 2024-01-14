first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0] + " " + line[1]
    nums = [int(x) for x in line[2:]]

    if "Add First" in command:
        first_set.update(nums)
    elif "Add Second" in command:
        second_set.update(nums)
    elif "Remove First" in command:
        first_set.difference_update(nums)
    elif "Remove Second" in command:
        second_set.difference_update(nums)
    elif "Check Subset" in command:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")