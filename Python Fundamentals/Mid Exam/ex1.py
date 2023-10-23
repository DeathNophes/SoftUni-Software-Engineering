xp_to_unlock_tank = float(input())
expected_battles = int(input())
tank_unlocked = False

gathered_xp = 0

battle_counter = 0
for battle in range(1, expected_battles + 1):
    battle_counter += 1
    curr_battle_xp = float(input())

    if battle % 3 == 0:
        curr_battle_xp *= 1.15
    if battle % 5 == 0:
        curr_battle_xp *= 0.90
    if battle % 15 == 0:
        curr_battle_xp *= 1.05

    gathered_xp += curr_battle_xp
    if gathered_xp >= xp_to_unlock_tank:
        tank_unlocked = True
        break

if tank_unlocked:
    print(f"Player successfully collected his needed experience for {battle_counter} battles.")
else:
    diff = abs(xp_to_unlock_tank - gathered_xp)
    print(f"Player was not able to collect the needed experience, {diff:.2f} more needed.")

