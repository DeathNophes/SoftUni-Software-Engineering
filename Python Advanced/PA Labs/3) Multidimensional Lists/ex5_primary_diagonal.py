rows = int(input())     # The matrix is a square
matrix = [[int(x) for x in input().split()] for row in range(rows)]

value = 0
for row_index in range(len(matrix)):
    value += matrix[row_index][row_index]
    # Because the matrix is a square

print(value)
