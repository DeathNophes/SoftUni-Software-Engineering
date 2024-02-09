rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]

sum_max = float("-inf")
sum_max_matrix = []

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        curr_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        below_element = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]

        curr_elements_sum = curr_element + next_element + below_element + diagonal_element
        if curr_elements_sum > sum_max:
            sum_max = curr_elements_sum
            sum_max_matrix = [[curr_element, next_element],
                              [below_element, diagonal_element]
                              ]

print(*sum_max_matrix[0])
print(*sum_max_matrix[1])
print(sum_max)
