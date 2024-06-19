rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split()]for j in range(rows)]

for col_index in range(cols):
    this_col_values = [row[col_index] for row in matrix]
    print(sum(this_col_values))
