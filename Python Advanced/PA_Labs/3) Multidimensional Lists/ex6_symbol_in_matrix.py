n = int(input())
matrix = [list(input()) for row in range(n)]
char = input()

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        curr_element = matrix[row_index][col_index]
        if curr_element == char:
            char_index = matrix[row_index].index(char)
            print(f"({row_index}, {char_index})")
            exit()

print(f"{char} does not occur in the matrix")
