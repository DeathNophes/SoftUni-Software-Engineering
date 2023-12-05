n = int(input())
word = input()
my_list = []
special_list =[]

for _ in range(n):
    sentence = input()
    my_list.append(sentence)
    if word in sentence:
        special_list.append(sentence)

print(my_list)
print(special_list)
