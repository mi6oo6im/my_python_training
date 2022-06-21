def shooting_range(targets: list):
    command = input()
    targets_count = 0
    while command != 'End':
        shot_index = int(command)
        if 0 <= shot_index < len(targets):
            shot_target = targets[shot_index]
            targets[shot_index] = -1
            for target in range(len(targets)):
                if targets[target] != -1:
                    if targets[target] <= shot_target:
                        targets[target] += shot_target
                    else:
                        targets[target] -= shot_target
            targets_count += 1
        command = input()
    print(f'Shot targets: {targets_count} -> ' + ' '.join([str(x) for x in targets]))


target_list = list(map(int, input().split()))
shooting_range(target_list)
