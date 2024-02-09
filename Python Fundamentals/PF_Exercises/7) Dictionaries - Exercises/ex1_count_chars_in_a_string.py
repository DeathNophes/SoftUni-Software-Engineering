words = input().split()
my_dict = {}

for word in words:
    for symbol in word:
        if symbol not in my_dict:
            my_dict[symbol] = 0
        my_dict[symbol] += 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")