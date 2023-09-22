shirt_price = float(input())
required_sum_for_ball = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = 2 * (shorts_price + shirt_price)

total_sum = shoes_price + shorts_price + socks_price + shirt_price
total_sum_after_discount = total_sum * 0.85

if total_sum_after_discount >= required_sum_for_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum_after_discount:.2f} lv.")
else:
    diff = abs(required_sum_for_ball - total_sum_after_discount)
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")
