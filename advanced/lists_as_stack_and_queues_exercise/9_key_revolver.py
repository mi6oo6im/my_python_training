from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
prize = int(input())

bullets_fired = 0
while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    bullets_fired += 1
    if current_lock >= current_bullet:
        print('Bang!')
    else:
        locks.appendleft(current_lock)
        print('Ping!')
    if bullets_fired % barrel_size == 0 and bullets:
        print('Reloading!')
earned = prize - (bullet_price * bullets_fired)
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${earned}")
