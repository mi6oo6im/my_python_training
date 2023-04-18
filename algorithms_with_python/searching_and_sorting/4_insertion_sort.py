nums = [int(x) for x in input().split()]
for i in range(len(nums)):
    for j in range(i, 0, -1):
        if nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
        # optimization - if we get to a point where the left is smaller than j we stop
        else:
            break

print(*nums, sep=' ')