from collections import deque

bees_queue = deque(int(x) for x in input().split())
nektar_stack = [int(x) for x in input().split()]
operators_queue = deque(input().split())
honey = 0

operation_dict = {
    '+': lambda x, y: abs(x + y),
    '*': lambda x, y: abs(x * y),
    '/': lambda x, y: abs(x / y) if y > 0 else 0,
    '-': lambda x, y: abs(x - y),
}

while bees_queue and nektar_stack:
    current_bee = bees_queue.popleft()
    current_nektar = nektar_stack.pop()
    if current_bee <= current_nektar:
        honey += operation_dict[operators_queue.popleft()](current_bee, current_nektar)
    else:
        bees_queue.appendleft(current_bee)
        continue
print(f"Total honey made: {honey}")
if bees_queue:
    print('Bees left:', end=' ')
    print(*bees_queue, sep=', ')
if nektar_stack:
    print('Nectar left:', end=' ')
    print(*nektar_stack, sep=', ')