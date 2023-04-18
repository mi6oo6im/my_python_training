def binary_search(nums_, tgt):
    left_idx = 0
    right_idx = len(nums_) - 1
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        mid_el = nums_[mid_idx]

        if mid_el == tgt:
            return mid_idx

        if tgt > mid_el:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return -1


nums = [int(x) for x in input().split()]
target = int(input())
print(binary_search(nums, target))
