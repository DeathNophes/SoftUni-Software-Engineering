n = int(input())

synonyms = {}

for _ in range(n):
    word = input()
    synonym = input()
    if word in synonyms:
        synonyms[word].append(synonym)
    # If we have the current word(key) in the dictionary we add the synonym(value) to a list
    else:
        synonyms[word] = [synonym]
    # Else we add the word as a key and create a list for the value

for word, synonym_list in synonyms.items():
    synonym_str = ', '.join(synonym_list)
    print(f"{word} - {synonym_str}")
