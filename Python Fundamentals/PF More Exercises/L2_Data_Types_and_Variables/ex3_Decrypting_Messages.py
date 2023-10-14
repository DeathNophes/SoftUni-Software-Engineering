key = int(input())
n = int(input())
my_list = []
for _ in range(n):
    symbol = input()
    my_list.append(chr(ord(symbol) + key))
print("".join(my_list))