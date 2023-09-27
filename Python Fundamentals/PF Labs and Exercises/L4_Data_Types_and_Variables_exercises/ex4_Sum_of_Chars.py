n = int(input())
total_sum = 0
for _ in range(n):
    current_character = input()
    total_sum += ord(current_character)
print(f"The sum equals: {total_sum}")
