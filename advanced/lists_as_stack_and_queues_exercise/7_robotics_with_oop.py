from collections import deque


class Robot:
    def __init__(self, name, time):
        self.name = name
        self.run_time = time
        self.busy = False
        self.busy_until = -1


def time_to_seconds(time: str):  # 8:00:00 to 28800
    time_list = [int(x) for x in time.split(':')]
    hours, minutes, seconds = time_list
    # hours = int(time_list[0])
    # minutes = int(time_list[1])
    # seconds = int(time_list[2])
    to_seconds = hours * 3600 + minutes * 60 + seconds
    return to_seconds


def time_to_string(time: int):
    hours = time // 3600
    minutes = (time - hours * 3600) // 60
    seconds = time - hours * 3600 - minutes * 60
    time_as_string = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    return time_as_string


full_day_to_seconds = 24 * 3600  # 86400
robots_list = deque()
robot_line = input().split(';')
for robot in robot_line:
    properties = robot.split('-')
    current_robot = Robot(properties[0], int(properties[1]))
    robots_list.append(current_robot)

starting_time = input()
real_time = time_to_seconds(starting_time)
details_queue = deque()

current_detail = input()
while current_detail != 'End':
    details_queue.append(current_detail)
    current_detail = input()

while details_queue:
    current_detail = details_queue.popleft()
    real_time += 1
    real_time %= full_day_to_seconds  # if we overhead the 24 hours

    # check if any robot has finished working on a detail
    for robot in robots_list:
        if robot.busy_until <= real_time:
            robot.busy = False

    # check if we have a free robot
    for robot in robots_list:
        if not robot.busy:
            robot.busy = True
            detail_time = time_to_string(real_time)
            robot.busy_until = real_time + robot.run_time
            robot.busy_until %= full_day_to_seconds
            print(f'{robot.name} - {current_detail} [{detail_time}]')
            break
    else:
        details_queue.append(current_detail)
