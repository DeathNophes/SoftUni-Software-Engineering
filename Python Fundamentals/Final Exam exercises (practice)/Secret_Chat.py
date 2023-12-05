message = input()
command = input()
while command != 'Reveal':
    command = command.split(':|:')
    if 'InsertSpace' in command:
        index = int(command[1])
        start_to_index = message[:index]
        index_to_end = message[index:]
        message = start_to_index + ' ' + index_to_end

    elif 'Reverse' in command:
        substring = command[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            message = message + substring[::-1]
        else:
            print('error')
            command = input()
            continue

    elif 'ChangeAll' in command:
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

    print(message)
    command = input()

print(f"You have a new text message: {message}")
