def are_they_in():
    my_list = [first_input_line[i] for i in range(len(first_input_line))
               if first_input_line[i] in second_input_line]
    return my_list


first_input_line = input().split(", ")
second_input_line = input()
print(are_they_in())
