sequence = [int(number) for number in input().split()]
avg_number = sum(sequence) / len(sequence)
greater_than_avg_nums = [num for num in sequence if num > avg_number]

if not greater_than_avg_nums:
    print("No")
    exit()

top_five_list = []

current_numbers = 0
for _ in range(len(greater_than_avg_nums)):
    current_max_num = max(greater_than_avg_nums)
    current_max_index = greater_than_avg_nums.index(current_max_num)
    this_max_num = greater_than_avg_nums.pop(current_max_index)
    top_five_list.append(this_max_num)
    current_numbers += 1
    if current_numbers == 5:
        break

for i in range(len(top_five_list)):
    print(top_five_list[i], end=" ")
