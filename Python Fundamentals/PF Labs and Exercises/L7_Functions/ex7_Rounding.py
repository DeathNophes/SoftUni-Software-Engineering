def rounded():
    float_list = []
    rounded_list = []
    for number in numbers:
        float_list.append(float(number))
    for number in float_list:
        rounded_list.append(round(number))
    return rounded_list


numbers = input().split()
print(rounded())