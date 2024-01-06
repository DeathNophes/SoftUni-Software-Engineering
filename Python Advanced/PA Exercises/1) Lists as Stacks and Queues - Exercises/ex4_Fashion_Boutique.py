clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
total_racks = 0

while clothes:
    curr_clothes = clothes.pop()
    while True:
        if curr_clothes == rack_capacity:
            total_racks += 1
            break
        if clothes:
            next_clothes = clothes.pop()
            curr_clothes += next_clothes
        else:
            total_racks += 1
            break
        if curr_clothes > rack_capacity:
            total_racks += 1
            clothes.append(next_clothes)
            break

print(total_racks)
