num_num = int(input())

even_sum = 0
odd_sum = 0

for i in range(1, num_num + 1):
    x = int(input())
    if i % 2 == 0:
        even_sum += x
    else:
        odd_sum += x

difference = abs(even_sum - odd_sum)

# output
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {difference}")
