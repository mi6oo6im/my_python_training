start = int(input())
end = int(input())

for i in range(start, end + 1):
    counter = 0
    odd_sum = 0
    even_sum = 0
    for j in str(i):
        counter += 1
        if counter % 2 == 0:
            even_sum += int(j)
        else:
            odd_sum += int(j)
    if even_sum == odd_sum:
        print(i, end=" ")
