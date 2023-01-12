numbers = int(input())
stack = []
map_funcs = {
    1: lambda x: stack.append(x[1]),
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}
for _ in range(numbers):
    command_list = [int(x) for x in input().split()]
    prefix = command_list[0]
    map_funcs[prefix](command_list)

if stack:
    stack.reverse()
    print(*stack, sep=', ')