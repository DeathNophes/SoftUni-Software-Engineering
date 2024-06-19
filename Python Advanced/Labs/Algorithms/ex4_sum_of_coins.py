def choose_coins(coins, target):
    coins.sort(reverse=True)
    idx = 0
    used_coins = {}     # coins: times used

    while target > 0 and idx < len(coins):
        count_curr_coins = target // coins[idx]     # 4,50 => 1 * 4
        target = target % coins[idx]                # 4,50 % 1 => 0.50

        if count_curr_coins > 0:
            used_coins[coins[idx]] = count_curr_coins

        idx += 1

    if target != 0:
        return "Error"
    else:
        result = f"Number of coins to take: {sum(used_coins.values())}\n"

        for value, count in used_coins.items():
            result += f"{count} coin(s) with value {value}\n"

        return result


coins_list = [int(x) for x in input().split(', ')]
target_num = int(input())
print(choose_coins(coins_list, target_num))