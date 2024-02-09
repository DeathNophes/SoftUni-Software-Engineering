first_line = input().split()
second_line = input().split()
third_line = input().split()
first_line = [int(num) for num in first_line]
second_line = [int(num) for num in second_line]
third_line = [int(num) for num in third_line]

if (first_line[0] == 1 and second_line[0] == 1 and third_line[0] == 1) \
        or (first_line[1] == 1 and second_line[1] == 1 and third_line[1] == 1) \
        or (first_line[2] == 1 and second_line[2] == 1 and third_line[2] == 1) \
        or (first_line[0] == 1 and second_line[1] == 1 and third_line[2] == 1) \
        or (first_line[2] == 1 and second_line[1] == 1 and third_line[0] == 1) \
        or (first_line.count(1) == 3 or second_line.count(1) == 3 or third_line.count(1) == 3):
    print("First player won")
elif (first_line[0] == 2 and second_line[0] == 2 and third_line[0] == 2) \
        or (first_line[1] == 2 and second_line[1] == 2 and third_line[1] == 2) \
        or (first_line[2] == 2 and second_line[2] == 2 and third_line[2] == 2) \
        or (first_line[0] == 2 and second_line[1] == 2 and third_line[2] == 2) \
        or (first_line[2] == 2 and second_line[1] == 2 and third_line[0] == 2) \
        or (first_line.count(2) == 3 or second_line.count(2) == 3 or third_line.count(2) == 3):
    print("Second player won")
else:
    print("Draw!")