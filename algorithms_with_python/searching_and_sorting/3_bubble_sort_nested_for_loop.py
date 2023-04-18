nums = [int(x) for x in input().split()]
for i in range(len(nums)):
    for j in range(1, len(nums) - i):
        if nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]

print(*nums, sep=' ')
