from collections import deque

COMMAND_PAID = 'Paid'
COMMAND_END = 'End'

customers_queue = deque()

command = input()
while not command == COMMAND_END:
    if command == COMMAND_PAID:
        length = len(customers_queue)
        for _ in range(length):
            print(customers_queue.popleft())
    else:
        customers_queue.append(command)
    command = input()
else:
    print(f'{len(customers_queue)} people remaining.')



