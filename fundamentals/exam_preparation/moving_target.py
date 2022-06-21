def shoot_func(index: int, power: int, targets: list):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    return targets


def add_func(index: int, value: int, targets: list):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")
    return targets


def strike_func(index: int, radius: int, targets: list):
    if 0 <= index - radius and index + radius < len(targets):
        targets = [targets[x] for x in range(len(targets)) if x < index - radius or x > index + radius]
    else:
        print('Strike missed!')
    return targets


def shooting_range(targets: list):
    command_line = input()
    while command_line != 'End':
        command, first_param, second_param = command_line.split()
        if command == 'Shoot':
            targets = shoot_func(int(first_param), int(second_param), targets)
        elif command == 'Add':
            targets = add_func(int(first_param), int(second_param), targets)
        elif command == 'Strike':
            targets = strike_func(int(first_param), int(second_param), targets)
        command_line = input()
    print(*targets, sep='|')


targets_list = list(map(int, input().split()))
shooting_range(targets_list)
