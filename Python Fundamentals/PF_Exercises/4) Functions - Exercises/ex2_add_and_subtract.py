def add(a, b):
    return a + b


def subtract(result, c):
    return result - c


def add_subtract(a, b, c):
    sum_a_b = add(a, b)
    final_result = subtract(sum_a_b, c)
    return final_result


first_num = int(input())
second_num = int(input())
third_num = int(input())
end_result = add_subtract(first_num, second_num, third_num)
print(end_result)
