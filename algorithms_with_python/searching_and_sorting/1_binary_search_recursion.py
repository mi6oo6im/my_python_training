def binary_search(nums_, tgt, left, right):
    mid = (left + right) // 2
    if left > right:
        print(-1)
        return
    if nums_[mid] == tgt:
        print(mid)
        return

    if tgt > nums_[mid]:
        binary_search(nums_, tgt, mid + 1, right)
    else:
        binary_search(nums_, tgt, left, mid - 1)


nums = [int(x) for x in input().split()]
target = int(input())
binary_search(nums, target, 0, len(nums) - 1)
