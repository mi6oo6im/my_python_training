from collections import deque

pumps = int(input())
stations_q = deque([[int(x) for x in input().split()] for _ in range(pumps)])
copy_of_stations_q = stations_q.copy()
tank = 0
index = 0

while copy_of_stations_q:
    current = copy_of_stations_q.popleft()
    fuel, distance = current
    tank += fuel
    if distance <= tank:
        tank -= distance
    else:
        stations_q.rotate(-1)
        copy_of_stations_q = stations_q.copy()
        index += 1
        tank = 0

print(index)
