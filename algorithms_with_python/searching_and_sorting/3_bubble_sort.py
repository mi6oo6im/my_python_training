nums = [int(x) for x in input().split()]
is_sorted = False

while not is_sorted:
    is_sorted = True
    counter = 0
    for idx in range(1, len(nums) - counter):
        if nums[idx] < nums[idx - 1]:
            nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx]
            is_sorted = False

        counter += 1

print(*nums, sep=' ')
