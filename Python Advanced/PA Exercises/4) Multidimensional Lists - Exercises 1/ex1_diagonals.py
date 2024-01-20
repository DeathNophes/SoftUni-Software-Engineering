rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]

primary_diagonal = [matrix[i][i] for i in range(rows)]
secondary_diagonal = [matrix[i][rows - i - 1] for i in range(rows)]

primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {secondary_sum}")
