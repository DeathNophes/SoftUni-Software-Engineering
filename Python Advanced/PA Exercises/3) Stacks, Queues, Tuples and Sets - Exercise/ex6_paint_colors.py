from collections import deque

colors_string = deque(input().split())

main_colors = ['red', 'blue', 'yellow']
secondary_colors = {'purple': ['red', 'blue'],
                    'orange': ['red', 'yellow'],
                    'green': ['blue', 'yellow']}
collected_colors = []

while colors_string:
    first_str = colors_string.popleft()
    last_str = colors_string.pop() if colors_string else ''     # If there is only one element we will get nothing
    result_1 = first_str + last_str
    result_2 = last_str + first_str
    if result_1 in main_colors or result_1 in secondary_colors.keys():
        collected_colors.append(result_1)
    elif result_2 in main_colors or result_2 in secondary_colors.keys():
        collected_colors.append(result_2)
    else:
        if len(first_str) > 1:
            colors_string.insert(len(colors_string) // 2, first_str[:-1])
        if len(last_str) > 1:
            colors_string.insert(len(colors_string) // 2, last_str[:-1])

for color in collected_colors:
    if color in secondary_colors.keys():
        for el in secondary_colors[color]:
            if el not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)