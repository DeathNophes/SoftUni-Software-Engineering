from collections import deque

matches = []
rotations = 0

seat_sequence = input().split(', ')
first_sequence = deque([int(x) for x in input().split(', ')])
second_sequence = deque([int(x) for x in input().split(', ')])

while len(matches) != 3 and rotations < 10:
    letter = chr(first_sequence[0] + second_sequence[-1])

    result1 = str(first_sequence[0]) + letter
    result2 = str(second_sequence[-1]) + letter

    if result1 in seat_sequence:
        matches.append(result1)
        first_sequence.popleft()
        second_sequence.pop()
        seat_sequence.remove(result1)

    elif result2 in seat_sequence:
        matches.append(result2)
        first_sequence.popleft()
        second_sequence.pop()
        seat_sequence.remove(result2)

    else:
        first_sequence.rotate(-1)
        second_sequence.rotate()

    rotations += 1

print(f"Seat matches: {', '.join(matches)}")
print(f"Rotations count: {rotations}")