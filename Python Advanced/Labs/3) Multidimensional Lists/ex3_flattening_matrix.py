rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
flattened = [el for sublist in matrix for el in sublist]
print(flattened)