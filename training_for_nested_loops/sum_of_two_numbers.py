a = int(input())
b = int(input())
m = int(input())
flag = False
counter = 0

for i in range(a, b + 1):
    for y in range(a, b + 1):
        counter += 1
        if i + y == m:
            flag = True
            break
    if flag:
        break

if flag:
    print(f"Combination N:{counter} ({i} + {y} = {m})")
else:
    print(f"{counter} combinations - neither equals {m}")
