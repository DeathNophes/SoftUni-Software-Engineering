numbers = list(map(int, input().split(", ")))
all_even_indexes = [x for x in range(len(numbers)) if numbers[x] % 2 == 0]
# Итерираме по дължината на листа, като ако намерим число, което е четно връщаме неговия индекс (х)
print(all_even_indexes)
