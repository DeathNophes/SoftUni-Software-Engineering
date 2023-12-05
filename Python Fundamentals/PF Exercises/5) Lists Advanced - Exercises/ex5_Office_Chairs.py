n = int(input())
free_chairs = 0
enough_chairs = True
for room in range(1, n + 1):
    data = input().split()
    chairs = data[0].count("X")
    visitors = int(data[1])
    if visitors <= chairs:
        free_chairs += abs(visitors - chairs)
    else:
        print(f"{abs(visitors - chairs)} more chairs needed in room {room}")
        enough_chairs = False

if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")
