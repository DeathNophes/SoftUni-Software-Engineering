array_of_integers = [int(num) for num in input().split()]

command = input()
while command != "end":
    command = command.split()

    if "swap" in command:
        index1 = int(command[1])
        index2 = int(command[2])
        array_of_integers[index1], array_of_integers[index2] = \
            array_of_integers[index2], array_of_integers[index1]

    elif "multiply" in command:
        index1 = int(command[1])
        index2 = int(command[2])
        array_of_integers[index1] *= array_of_integers[index2]

    elif "decrease" in command:
        for num in range(len(array_of_integers)):
            array_of_integers[num] -= 1

    command = input()

array_of_str = [str(symbol) for symbol in array_of_integers]
print(", ".join(array_of_str))
