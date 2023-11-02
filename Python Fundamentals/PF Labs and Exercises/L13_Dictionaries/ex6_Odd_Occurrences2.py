words = [word.lower() for word in input().split()]
# Makes the words in lower case
my_dict = {}

for word in words:
    if word not in my_dict:
        my_dict[word] = 0  # We create the new key=value
    my_dict[word] += 1  # We add one more to the value

    # We use the word as a key and the number of occurrences as a value

for key, value in my_dict.items():
    if value % 2 == 1:
        print(f"{key}", end=' ')
