def selection_sort(nums_):
    for idx in range(len(nums_)):
        current_num = nums_[idx]
        min_num = current_num
        min_idx = idx
        for next_idx in range(idx + 1, len(nums_)):
            if min_num > nums_[next_idx]:
                min_num = nums_[next_idx]
                min_idx = next_idx
        nums_[idx], nums_[min_idx] = nums_[min_idx], nums_[idx]

    return nums_


nums = [int(x) for x in input().split()]
sorted_nums = selection_sort(nums)
print(*sorted_nums, sep=' ')

