from datetime import datetime, timedelta
from collections import deque

robots = {name: [int(process_time), 0] for name, process_time in [robot.split('-') for robot in input().split(';')]}

time = datetime.strptime(input(), '%H:%M:%S')

products = deque()
current_product = input()
while not current_product == 'End':
    products.append(current_product)
    current_product = input()
while products:
    time = time + timedelta(seconds=1)
    current = products.popleft()
    avail_robots = []
    for name, value in robots.items():
        if not value[1] == 0:
            robots[name][1] -= 1
            if robots[name][1] == 0:
                avail_robots.append([name, value])
        else:
            avail_robots.append([name, value])

    if not avail_robots:
        products.append(current)
        continue
    robot_name, data = avail_robots[0]
    robots[robot_name][1] = data[0]
    print(f'{robot_name} - {current} [{time.strftime("%H:%M:%S")}]')
    continue
