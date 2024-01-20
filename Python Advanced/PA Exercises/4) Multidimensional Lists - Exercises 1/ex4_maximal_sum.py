rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for row in range(rows)]

max_sum = float('-inf')
max_sum_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_el = matrix[row][col]
        second_el = matrix[row][col + 1]
        third_el = matrix[row][col + 2]
        fourth_el = matrix[row + 1][col]
        fifth_el = matrix[row + 1][col + 1]
        sixth_el = matrix[row + 1][col + 2]
        seventh_el = matrix[row + 2][col]
        eighth_el = matrix[row + 2][col + 1]
        ninth_el = matrix[row + 2][col + 2]

        result = first_el + second_el + third_el + fourth_el + fifth_el \
                 + sixth_el + seventh_el + eighth_el + ninth_el

        if result > max_sum:
            max_sum = result
            max_sum_matrix = [[first_el, second_el, third_el],
                              [fourth_el, fifth_el, sixth_el],
                              [seventh_el, eighth_el, ninth_el]
                              ]
print(f"Sum = {max_sum}")
[print(*row) for row in max_sum_matrix]
