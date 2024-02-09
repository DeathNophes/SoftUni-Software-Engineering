rows = int(input())

even_matrix = []

for _ in range(rows):
    elements = [int(x) for x in input().split(', ') if int(x) % 2 == 0]
    even_matrix.append(elements)

print(even_matrix)
