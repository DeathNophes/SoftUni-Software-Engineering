dancers = int(input())
points = float(input())
season = input()
country = input()

earned_money = 0
money_after_seasons = 0

if country == 'Bulgaria':
    earned_money = dancers * points
    if season == 'summer':
        money_after_seasons = earned_money * 0.95
    elif season == 'winter':
        money_after_seasons = earned_money * 0.92
elif country == 'Abroad':
    earned_money = (dancers * points) + (0.50 * (dancers * points))
    if season == 'summer':
        money_after_seasons = earned_money * 0.90
    elif season == 'winter':
        money_after_seasons = earned_money * 0.85

money_for_charity = 0.75 * money_after_seasons
left_money = money_after_seasons - money_for_charity
money_per_dancer = left_money / dancers

print(f"Charity - {money_for_charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")