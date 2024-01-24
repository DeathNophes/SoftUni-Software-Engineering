line = input().split('|')   # ['7 88', '4   5 6', '1 2   3']

sub_lists = []  # [1, 2, 3].extend([4, 5, 6]) -> [1, 2, 3, 4, 5, 6]

for sub_string in line[::-1]:
    sub_lists.extend(sub_string.split())  # '4    5 6' -> [4, 5, 6]

print(*sub_lists)
