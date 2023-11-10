phonebook = {}

while True:
    entry = input()
    if entry.isdigit():
        break
    person, number = entry.split("-")
    phonebook[person] = number

for _ in range(int(entry)):
    name = input()
    if name in phonebook.keys():
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
