n = int(input())
counter = 0
for i in range (n+1):
    for y in range (n+1):
        for j in range(n+1):
            if i + y + j == n:
                counter += 1
                break
print(counter)
