words = [word.lower() for word in input().split()]
my_dict = []

for word in words:
    word = word.lower()
    if word not in my_dict:
        this_element_count = words.count(word)
        if this_element_count % 2 == 1:
            my_dict.append(word)

print(" ".join(my_dict))
