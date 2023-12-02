raw_activation_key = input()
command = input()

while command != 'Generate':
    command = command.split(">>>")

    if 'Contains' in command:
        substring = command[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif 'Flip' in command:
        startIndex = int(command[2])
        endIndex = int(command[3])
        if command[1] == 'Upper':
            raw_activation_key = raw_activation_key[:startIndex] + \
                                 raw_activation_key[startIndex:endIndex].upper() + \
                                 raw_activation_key[endIndex:]
            print(raw_activation_key)

        elif command[1] == 'Lower':
            raw_activation_key = raw_activation_key[:startIndex] + \
                                 raw_activation_key[startIndex:endIndex].lower() + \
                                 raw_activation_key[endIndex:]
            print(raw_activation_key)

    elif 'Slice' in command:
        startIndex = int(command[1])
        endIndex = int(command[2])
        raw_activation_key = raw_activation_key[:startIndex] + raw_activation_key[endIndex:]
        print(raw_activation_key)

    command = input()

print(f"Your activation key is: {raw_activation_key}")