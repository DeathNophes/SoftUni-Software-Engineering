circle = input().split()
k = int(input())
circle_int = [int(person) for person in circle]
execution_list = []
counter = 0

index = 0
while circle_int:
    counter += 1
    if counter % k == 0:
        execution_list.append(circle_int[index])
        circle_int.pop(index)
    else:
        index += 1

    if index >= len(circle_int):
        index = 0
print(str(execution_list).replace(" ", ""))