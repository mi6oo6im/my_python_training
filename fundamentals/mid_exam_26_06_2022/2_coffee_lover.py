def include_func(coffee_list: list, coffee_to_include: str):
    coffee_list.append(coffee_to_include)
    return coffee_list


def remove_func(coffee_list: list, first_last: str, coffees_to_remove: int):
    if first_last == 'first':
        for _ in range(coffees_to_remove):
            coffee_list.pop(0)
    else:
        for _ in range(coffees_to_remove):
            coffee_list.pop(-1)
    return coffee_list


def prefer_func(coffee_list: list, first_coffee: int, second_coffee: int):
    coffee_list[first_coffee], coffee_list[second_coffee] = coffee_list[second_coffee], coffee_list[first_coffee]
    return coffee_list


def reverse_func(coffee_list: list):
    return reversed(coffee_list)


def coffee_manipulation_func(coffee_list: list, commands: int):
    for _ in range(commands):
        command_line = input().split()
        command = command_line[0]
        if command == 'Include':
            include_coffee = command_line[1]
            coffee_list = include_func(coffee_list, include_coffee)
        elif command == 'Remove':
            first_or_last = command_line[1]
            count_to_remove = int(command_line[2])
            if count_to_remove <= len(coffee_list):
                coffee_list = remove_func(coffee_list, first_or_last, count_to_remove)
        elif command == 'Prefer':
            index_1 = int(command_line[1])
            index_2 = int(command_line[2])
            if 0 <= index_1 < len(coffee_list) and 0 <= index_2 < len(coffee_list):
                coffee_list = prefer_func(coffee_list, index_1, index_2)
        elif command == 'Reverse':
            coffee_list = reverse_func(coffee_list)
    print('Coffees:')
    print(*coffee_list)


coffees = input().split()
number_of_commands = int(input())
coffee_manipulation_func(coffees, number_of_commands)
