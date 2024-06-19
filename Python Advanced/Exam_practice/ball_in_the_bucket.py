def get_the_prize(points):
    if points < 100:
        diff = 100 - points
        return f"Sorry! You need {diff} points more to win a prize."

    elif 100 <= points <= 199:
        return f"Good job! You scored {points} points, and you've won Football."

    elif 200 <= points <= 299:
        return f"Good job! You scored {points} points, and you've won Teddy Bear."

    elif points >= 300:
        return f"Good job! You scored {points} points, and you've won Lego Construction Set."


SIZE = 6

matrix = []

total_points = 0

for row in range(SIZE):
    matrix.append(input().split())

for _ in range(3):
    coordinates = input()
    coordinates = coordinates.replace(' ', '')
    coordinates = coordinates.replace('(', '')
    coordinates = coordinates.replace(')', '')
    coordinates = tuple(map(int, coordinates.split(',')))

    row, col = coordinates

    if not (0 <= row < SIZE and 0 <= col < SIZE):
        continue

    if matrix[row][col] == 'B':
        matrix[row][col] = 'x'
        for new_row in range(SIZE):
            if matrix[new_row][col].isdigit():
                total_points += int(matrix[new_row][col])

print(get_the_prize(total_points))
