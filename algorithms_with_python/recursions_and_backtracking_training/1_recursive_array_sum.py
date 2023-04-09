def recursive_array_sum(num_list: list, idx: int) -> int:
    if idx == len(num_list) - 1:
        return num_list[idx]

    return num_list[idx] + recursive_array_sum(num_list, idx + 1)


nums = [int(x) for x in input().split()]
print(recursive_array_sum(nums, 0))
