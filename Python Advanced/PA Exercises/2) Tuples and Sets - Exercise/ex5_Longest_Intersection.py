n = int(input())
longest_intersection = set()
for _ in range(n):
    first_nums, second_nums = input().split('-')
    first_start, first_end = [int(x) for x in first_nums.split(',')]
    second_start, second_end = [int(x) for x in second_nums.split(',')]

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    current_intersection = first_set & second_set
    # Intersection

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

length = len(longest_intersection)
print(f"Longest intersection is {list(longest_intersection)} with length {length}")
