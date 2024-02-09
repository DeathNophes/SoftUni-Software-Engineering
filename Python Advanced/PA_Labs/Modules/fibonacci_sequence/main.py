from core import create_fibonacci, locate

last_sequence = []
while True:
    command = input()
    if command == 'Stop':
        break

    data = command.split()

    if data[0] == 'Create':
        count = int(data[-1])
        last_sequence = create_fibonacci(count)
        print(' '.join(str(x) for x in last_sequence))

    elif data[0] == 'Locate':
        number = int(data[-1])
        print(locate(number, last_sequence))