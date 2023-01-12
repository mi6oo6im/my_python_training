from collections import deque

kids_q = deque(input().split())
rotation = int(input())

while len(kids_q) > 1:
    # kids_q.rotate(-rotation)
    for _ in range(rotation):
        kids_q.append(kids_q.popleft())
    burned_kid = kids_q.pop()
    print(f'Removed {burned_kid}')
print(f'Last is {kids_q[0]}')
