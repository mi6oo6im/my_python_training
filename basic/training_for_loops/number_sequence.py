import sys

num_nums = int(input())

min_num = sys.maxsize
max_num = -sys.maxsize

for i in range(0, num_nums):
    x = int(input())
    if x > max_num:
        max_num = x
    if x < min_num:
        min_num = x

# output
print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
