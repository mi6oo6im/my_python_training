import sys
from collections import deque

food_qty = int(input())
orders_q = deque([int(x) for x in input().split()])
max_order = -sys.maxsize
for order in orders_q:
    if max_order < order:
        max_order = order

print(max_order)

while orders_q:
    current_order = orders_q[0]
    if food_qty >= current_order:
        food_qty -= orders_q.popleft()
    else:
        break
else:
    print('Orders complete')
if orders_q:
    print(f'Orders left: ', end='')
    print(*orders_q)
