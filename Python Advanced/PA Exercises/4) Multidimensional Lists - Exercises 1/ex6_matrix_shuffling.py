rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

command = input()
while command != 'END':
    data = command.split()
    if data[0] == 'swap' and len(data) == 5:
        if int(data[1]) < rows and int(data[3]) < rows and int(data[2]) < cols and int(data[4]) < cols:
            row1 = int(data[1])
            col1 = int(data[2])
            row2 = int(data[3])
            col2 = int(data[4])
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            [print(*row) for row in matrix]
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
    command = input()