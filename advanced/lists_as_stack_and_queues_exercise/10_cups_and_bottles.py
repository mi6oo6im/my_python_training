from collections import deque

cups_queue = deque(int(x) for x in input().split())
bottles_stack = [int(x) for x in input().split()]
waisted_watter = 0

while cups_queue and bottles_stack:
    current_cup = cups_queue.popleft()
    current_bottle = bottles_stack.pop()
    if current_cup > current_bottle:
        current_cup -= current_bottle
        cups_queue.appendleft(current_cup)
    else:
        waisted_watter += current_bottle - current_cup

if bottles_stack:
    reversed_bottles = reversed(bottles_stack)
    print('Bottles:', *reversed_bottles)
else:
    print('Cups:', *cups_queue)
print(f"Wasted litters of water: {waisted_watter}")