def recursion(num_list: list, index: int):
    if index == len(num_list) - 1:
        return num_list[index]
    return num_list[index] + recursion(num_list, index + 1)


input_array = [int(x) for x in input().split()]

print(recursion(input_array, 0))
