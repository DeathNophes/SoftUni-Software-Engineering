def take_odd(curr_password: str):
    new_password = ''
    for i in range(1, len(curr_password), 2):
        new_password += curr_password[i]
    return new_password


def cut(_index, _length, curr_password):
    new_password = curr_password[:_index] + curr_password[_index + _length:]
    return new_password


def sub(_substring: str, _substitute: str, curr_password: str):
    new_password = curr_password.replace(_substring, _substitute)
    return new_password


password = input()
command = input()
while command != 'Done':
    command = command.split()
    if 'TakeOdd' in command:
        password = take_odd(password)
        print(password)

    elif 'Cut' in command:
        index = int(command[1])
        length = int(command[2])
        new_pass = cut(index, length, password)
        password = new_pass
        print(password)

    elif 'Substitute' in command:
        substring = command[1]
        substitute = command[2]
        if substring in password:
            new_pass = sub(substring, substitute, password)
            password = new_pass
            print(password)
        else:
            print('Nothing to replace!')

    command = input()

print(f"Your password is: {password}")
