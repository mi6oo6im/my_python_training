def reverse_arr_recursive(left_idx, nums):
    if left_idx == len(nums) // 2:
        return

    right_idx = len(nums) - 1 - left_idx
    nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]

    reverse_arr_recursive(left_idx + 1, nums)


def reverse_arr_iterative(nums):
    for i in range(len(nums) // 2):
        right_idx = i
        left_idx = len(nums) - 1 - i
        nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]

    return nums


arr = input().split()
# reverse_arr_recursive(0, arr)
# print(' '.join(arr))

print(' '.join(reverse_arr_iterative(arr)))


