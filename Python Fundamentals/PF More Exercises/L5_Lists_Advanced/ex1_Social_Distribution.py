def what_is_max():
    max_num = max(population)
    max_index_ = population.index(max_num)
    return max_index_


population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

for i in range(len(population)):
    if population[i] < minimum_wealth:
        max_index = what_is_max()
        if max_index < i:
            print("No equal distribution possible")
            exit()
        diff = minimum_wealth - population[i]
        population[i] += diff
        population[max_index] -= diff

print(population)
