def loading_bar(num: int):
    if num == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    x = num // 10
    percentages = '%' * x
    dots = '.' * (10 - x)
    return f"{num}% [{percentages}{dots}]\nStill loading..."


number = int(input())
print(loading_bar(number))
