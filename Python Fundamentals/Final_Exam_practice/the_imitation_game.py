message = input()
command = input()
while command != 'Decode':
    command = command.split('|')
    if 'Move' in command:
        number_of_letters = int(command[1])
        message = message[number_of_letters:] + message[:number_of_letters]

    elif 'Insert' in command:
        index = int(command[1])
        value = command[2]
        message_after_index = message[index:]
        message = message[:index] + value + message_after_index
        # We add the value at the required index

    elif 'ChangeAll' in command:
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

    command = input()

print(f"The decrypted message is: {message}")
