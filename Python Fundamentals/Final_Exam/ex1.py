text = input()
command = input()
while command != 'Done':
    command = command.split()
    if 'Change' in command:
        char = command[1]
        replacement = command[2]
        text = text.replace(char, replacement)
        print(text)

    elif 'Includes' in command:
        substring = command[1]
        if substring in text:
            print('True')
        else:
            print('False')

    elif 'End' in command:
        substring = command[1]
        if text.endswith(substring):
            print('True')
        else:
            print('False')

    elif 'Uppercase' in command:
        text = text.upper()
        print(text)

    elif 'FindIndex' in command:
        char = command[1]
        a = text.index(char)
        print(a)

    elif 'Cut' in command:
        startIndex = int(command[1])
        count = int(command[2])
        cut_chars = text[startIndex:startIndex + count]
        print(cut_chars)

    command = input()