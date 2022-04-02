half_num_num = int(input())

left_sum = 0
right_sum = 0

for i in range(1, half_num_num * 2 + 1):
    x = int(input())
    if i <= half_num_num:
        left_sum += x
    else:
        right_sum += x


difference = abs(left_sum-right_sum)
# output

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {difference}")
