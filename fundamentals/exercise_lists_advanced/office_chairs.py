def chairs_visitors(room_chairs: str):
    chairs, visitors = room_chairs.split()
    return len(chairs), int(visitors)


def enough_chairs_check(room: int, chair_num: int, visitor_num: int):
    if chair_num < visitor_num:
        diff = abs(chair_num - visitor_num)
        print(f'{diff} more chairs needed in room {room}')
        return False, chair_num, visitor_num
    return True, chair_num, visitor_num


total_chairs = 0
total_visitors = 0
rooms = int(input())
chairs_are_enough = True
for room in range(1, rooms + 1):
    chair_num, visitor_num = chairs_visitors(input())
    current_chairs_are_enough, current_chair_num, current_visitor_num =\
        enough_chairs_check(room, chair_num, visitor_num)
    if not current_chairs_are_enough:
        chairs_are_enough = False
    total_chairs += current_chair_num
    total_visitors += current_visitor_num
total_free_chairs = total_chairs - total_visitors
if chairs_are_enough:
    print(f'Game On, {total_free_chairs} free chairs left')
