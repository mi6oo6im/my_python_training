from collections import deque
presents_crafted = {}
presents_dict = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}
materials_stack = [int(x) for x in input().split()]
magic_queue = deque(int(x) for x in input().split())

while materials_stack and magic_queue:
    current_mat = materials_stack.pop()
    current_mag = magic_queue.popleft()
    if current_mag == 0 and current_mat == 0:
        continue
    elif current_mag == 0:
        materials_stack.append(current_mat)
        continue
    elif current_mat == 0:
        magic_queue.appendleft(current_mag)
        continue
    score = current_mat * current_mag
    if score in presents_dict.keys():
        current_present = presents_dict[score]
        if current_present not in presents_crafted.keys():
            presents_crafted[current_present] = 0
        presents_crafted[current_present] += 1
    elif score < 0:
        materials_stack.append(current_mat + current_mag)
    else:
        current_mat += 15
        materials_stack.append(current_mat)

if ('Doll' in presents_crafted.keys() and 'Wooden train' in presents_crafted.keys()) or\
        ('Teddy bear' in presents_crafted.keys() and 'Bicycle' in presents_crafted.keys()):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_stack:
    print('Materials left: ', end='')
    print(*reversed(materials_stack), sep=', ')
if magic_queue:
    print('Magic left: ', end='')
    print(*magic_queue, sep=', ')
print(*[f'{toy}: {amount}'for toy, amount in sorted(presents_crafted.items())], sep='\n')
