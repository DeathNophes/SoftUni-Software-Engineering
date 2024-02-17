from collections import deque

money = [int(x) for x in input().split()]
prices = deque([int(x) for x in input().split()])

foods_eaten = 0

while money and prices:

    if money[-1] == prices[0]:
        foods_eaten += 1
        money.pop()
        prices.popleft()

    elif money[-1] > prices[0]:
        foods_eaten += 1
        change = money[-1] - prices[0]
        money.pop()
        prices.popleft()
        if money:
            money[-1] += change

    elif money[-1] < prices[0]:
        money.pop()
        prices.popleft()

if foods_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {foods_eaten} foods.")
elif 1 < foods_eaten < 4:
    print(f"Henry ate: {foods_eaten} foods.")
elif foods_eaten == 1:
    print(f"Henry ate: {foods_eaten} food.")
elif foods_eaten == 0:
    print("Henry remained hungry. He will try next weekend again.")