input_nums = [int(x) for x in input().split()]
length = len(input_nums)
for _ in range(length):
    print(input_nums.pop(), end=' ')