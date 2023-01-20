from collections import deque

numbers_q = deque(int(x) for x in input().split())
target = int(input())
while numbers_q:
    operand_1 = numbers_q.popleft()
    temp = deque()
    match_is_found = False
    while numbers_q:
        operand_2 = numbers_q.popleft()
        if operand_1 + operand_2 == target:
            match_is_found = True
            print(f'{operand_1} + {operand_2} = {target}')
            break
        temp.append(operand_2)
    temp.extend(numbers_q)
    numbers_q = temp
