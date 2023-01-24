from collections import deque
from functools import reduce

input_string = input()
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y
}
queue = deque(int(x) if x[-1].isdigit() else x for x in input_string.split())
result = None
nums = deque()
while queue:
    current = queue.popleft()
    if current in operations.keys():
        result = reduce(operations[current], nums)
        queue.appendleft(result)
        nums = deque()
    else:
        nums.append(current)
print(result)
