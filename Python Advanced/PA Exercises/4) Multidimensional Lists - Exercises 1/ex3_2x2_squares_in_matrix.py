rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for row in range(rows)]

square_matrices_count = 0

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        if matrix[row_index][col_index] == matrix[row_index][col_index + 1]\
                == matrix[row_index + 1][col_index]\
                == matrix[row_index + 1][col_index + 1]:
            square_matrices_count += 1

print(square_matrices_count)
