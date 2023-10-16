def check_happiness():
    happiness_list = list(map(int, input().split()))
    # Използваме map, за да превърнем всеки елемент в листа от str -> int
    happiness_factor = int(input())

    improved_happiness = [happiness * happiness_factor for happiness in happiness_list]
    # Умножаваме щастието по съответния фактор за всеки човек в листа
    avg_happiness = sum(improved_happiness) / len(improved_happiness)
    # Изчисляваме средната стойност на щастието
    happy_count = sum(happiness >= avg_happiness for happiness in improved_happiness)
    # Щастливи са хората, които имат над средното ниво на щастие, затова искаме техния брой
    total_count = len(improved_happiness)

    message = 'happy' if happy_count >= (len(improved_happiness) / 2) else 'not happy'
    result = f"Score: {happy_count}/{total_count}. Employees are {message}!"
    return result


print(check_happiness())
