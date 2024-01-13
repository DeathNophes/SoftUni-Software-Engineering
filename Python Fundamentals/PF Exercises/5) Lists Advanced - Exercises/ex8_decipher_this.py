words = input().split()
for word in words:
    this_number_as_str = ""
    this_word_in_list = []
    for i in range(len(word)):
        if word[i].isdigit():
            this_number_as_str += word[i]
        else:
            this_word_in_list.append(word[i])
    this_word_in_list[0], this_word_in_list[-1] = this_word_in_list[-1], this_word_in_list[0]
    this_word = "".join(this_word_in_list)
    this_number = chr(int(this_number_as_str))
    print(this_number + this_word, end=" ")
