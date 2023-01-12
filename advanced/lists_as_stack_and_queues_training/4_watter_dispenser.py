from collections import deque

water = int(input())
drinkers = deque()
name = input()
while not name == 'Start':
    drinkers.append(name)
    name = input()

command = input()
while not command == 'End':
    if command.startswith('refill'):
        refill = int(command.split()[1])
        water += refill
    else:
        drank = int(command)
        if water >= drank:
            water -= drank
            print(f'{drinkers.popleft()} got water')
        else:
            print(f'{drinkers.popleft()} must wait')
    command = input()
print(f'{water} liters left')
