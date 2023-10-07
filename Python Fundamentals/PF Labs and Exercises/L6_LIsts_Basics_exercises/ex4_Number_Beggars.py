money_as_str = input().split(', ')
beggars = int(input())
money_as_int = []
for curr_money in money_as_str:
    money_as_int.append(int(curr_money))
final_sums = []
start_index = 0
for beggar in range(beggars):
    current_beggar_sum = 0
    for curr_index in range(start_index, len(money_as_int), beggars):
        current_beggar_sum += money_as_int[curr_index]
    final_sums.append(current_beggar_sum)
    start_index += 1
print(final_sums)
