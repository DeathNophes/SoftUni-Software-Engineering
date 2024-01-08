from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(y) for y in input().split())
intelligence_value = int(input())

bullets_count = 0
bullets_in_barrel = gun_barrel_size
got_the_intelligence = False

while True:
    curr_bullet = bullets.pop()
    bullets_in_barrel -= 1
    bullets_count += 1
    current_lock = locks.popleft()

    if curr_bullet <= current_lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.insert(0, current_lock)

    if bullets_in_barrel == 0 and bullets:
        print("Reloading!")
        if len(bullets) >= gun_barrel_size:
            bullets_in_barrel = gun_barrel_size
        else:
            bullets_in_barrel = len(bullets)

    if not locks:
        got_the_intelligence = True
        break

    if locks and not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break

if got_the_intelligence:
    earned_money = intelligence_value - (bullets_count * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")