n = int(input())
nums_list = [int(input()) for _ in range(n)]

filtered_list = []
command = input()
if command == 'even':
    for i in nums_list:
        if i % 2 == 0 or i == 0:
            filtered_list.append(i)
elif command == 'odd':
    for i in nums_list:
        if i % 2 == 1:
            filtered_list.append(i)
elif command == 'negative':
    for i in nums_list:
        if i < 0:
            filtered_list.append(i)
elif command == 'positive':
    for i in nums_list:
        if i >= 0:
            filtered_list.append(i)

print(filtered_list)
