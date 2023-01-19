from collections import deque

green, yellow = [int(input()) for _ in range(2)]
cars_passed = 0
car = input()
crashed = False
car_queue = deque()
crashed_at_char = None
while not car == 'END':
    if not car == 'green':
        car_queue.append(car)
    else:
        current_green = green
        queue_len = len(car_queue)
        for _ in range(queue_len):
            car = car_queue.popleft()
            length = len(car)
            if length < current_green:
                current_green -= length
                cars_passed += 1
                continue
            elif length <= current_green + yellow:
                cars_passed += 1
                break
            else:
                crashed = True
                crashed_at_char = current_green + yellow
                break
    if crashed:
        break
    car = input()
if crashed:
    print('A crash happened!')
    print(f'{car} was hit at {car[crashed_at_char]}.')
else:
    print('Everyone is safe.')
    print(f'{cars_passed} total cars passed the crossroads.')
