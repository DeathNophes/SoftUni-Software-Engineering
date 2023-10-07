numbers_list = input().split()
remover = int(input())
my_list = []

for number in numbers_list:
    my_list.append(int(number))


for num1 in range(remover):
    my_list.remove(min(my_list))

print(*my_list, sep=", ")
