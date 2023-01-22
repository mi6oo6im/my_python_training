first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())
num_commands = int(input())
for _ in range(num_commands):
    command_1, command_2, *data = [int(x) if x.isdigit() else x for x in input().split()]
    if command_1 == 'Add':
        if command_2 == 'First':
            for num in data:
                first_set.add(num)
        else:
            for num in data:
                second_set.add(num)
    elif command_1 == 'Remove':
        if command_2 == 'First':
            for num in data:
                first_set.discard(num)
        else:
            for num in data:
                second_set.discard(num)
    else:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
