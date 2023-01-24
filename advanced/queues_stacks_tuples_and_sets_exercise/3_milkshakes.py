from collections import deque

choco_stack = [int(x) for x in input().split(', ')]
milk_queue = deque(int(x) for x in input().split(', '))
milk_shakes = 0

while choco_stack and milk_queue and milk_shakes < 5:
    current_milk = milk_queue.popleft()
    current_choco = choco_stack.pop()
    if current_milk <= 0 and current_choco <= 0:
        continue
    elif current_milk <= 0 and not current_choco <= 0:
        choco_stack.append(current_choco)
        continue
    elif not current_milk <= 0 and current_choco <= 0:
        milk_queue.appendleft(current_milk)
        continue
    if current_milk == current_choco:
        milk_shakes += 1
        continue
    else:
        milk_queue.append(current_milk)
        choco_stack.append(current_choco - 5)
if milk_shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if choco_stack:
    print("Chocolate: ", end='')
    print(*choco_stack, sep=', ')
else:
    print("Chocolate: empty")
if milk_queue:
    print("Milk: ", end='')
    print(*milk_queue, sep=', ')
else:
    print("Milk: empty")
