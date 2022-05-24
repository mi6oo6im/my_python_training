import sys

max_num = -sys.maxsize

num_num = int(input())

result = 0
for i in range(num_num):
    x = int(input())
    if x > max_num:
        max_num = x
    result += x

result -= max_num

difference = abs(result - max_num)

if result == max_num:
    print("Yes")
    print(f"Sum = {result}")
else:
    print("No")
    print(f"Diff = {difference}")
