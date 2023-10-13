lenght = int(input())
width = int(input())
height = int(input())
percent_dec = float(input())
# Декорацията в аквариума ще заема част от обема

volume = lenght * width * height
# измерваме обема в см3
total_lt = volume / 1000
# Превръщаме от см3 в литри (1л = 1дм3)
dec_volume = total_lt * (percent_dec / 100)

result = total_lt - dec_volume

print(result)