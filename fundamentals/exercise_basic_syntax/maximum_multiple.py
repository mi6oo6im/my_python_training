multiplier = int(input())
boundary = int(input())
max_multiplier = 0
for i in range(1, boundary + 1):
    if max_multiplier < i and i % multiplier == 0:
        max_multiplier = i
print(max_multiplier)
