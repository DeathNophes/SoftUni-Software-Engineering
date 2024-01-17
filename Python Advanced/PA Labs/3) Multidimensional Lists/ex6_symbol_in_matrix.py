n = int(input())
matrix = [list(input()) for row in range(n)]
char = input()

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == char:
            print(f"({row}, {matrix[row].index(char)})")
            exit()

print(f"{char} does not occur in the matrix")
