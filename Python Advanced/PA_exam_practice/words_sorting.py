def words_sorting(*args):
    result = ""
    words_dict = {}
    combined_values = 0

    for word in args:
        words_dict[word] = 0
        for symbol in word:
            words_dict[word] += ord(symbol)

    for value in words_dict.values():
        combined_values += value

    if combined_values % 2 == 0:
        sorted_words_dict = sorted(words_dict.items(), key=lambda x: x[0])
    else:
        sorted_words_dict = sorted(words_dict.items(), key=lambda x: -x[1])

    for key, value in sorted_words_dict:
        result += f"{key} - {value}\n"

    return result
