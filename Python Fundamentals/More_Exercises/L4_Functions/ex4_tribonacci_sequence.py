def tribonacci_sequence(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    elif n == 2:
        return "1 1"
    elif n == 3:
        return "1 2"
    starting_list = [1, 1, 2]
    for i in range(n - 3):
        starting_list.append(sum(starting_list[i:i + 3]))
    my_list = list(map(str, starting_list))
    result = " ".join(my_list)
    return result


number = int(input())
print(tribonacci_sequence(number))