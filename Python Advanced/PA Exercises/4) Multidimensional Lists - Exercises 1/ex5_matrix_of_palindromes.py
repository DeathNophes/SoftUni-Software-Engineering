rows, cols = [int(x) for x in input().split()]

matrix = []
letters = 'abcdefghijklmnopqrstuvwxyz'

for row_index in range(rows):
    counter = row_index
    matrix.append([])
    for col_index in range(cols):
        matrix[row_index].append(letters[row_index] + letters[counter] + letters[row_index])
        counter += 1

[print(*row) for row in matrix]
