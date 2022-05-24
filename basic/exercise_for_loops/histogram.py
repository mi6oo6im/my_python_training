num_num = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
result = 0
p1percent = 0.0
p2percent = 0.0
p3percent = 0.0
p4percent = 0.0
p5percent = 0.0

for i in range(num_num):
    x = int(input())
    result += 1
    if x < 200:
        p1 += 1
    elif x < 400:
        p2 += 1
    elif x < 600:
        p3 += 1
    elif x < 800:
        p4 += 1
    else:
        p5 += 1

if p1 != 0:
    p1percent = p1 / result * 100
if p2 != 0:
    p2percent = p2 / result * 100
if p3 != 0:
    p3percent = p3 / result * 100
if p4 != 0:
    p4percent = p4 / result * 100
if p5 != 0:
    p5percent = p5 / result * 100

print(f"{p1percent:.2f}%")
print(f"{p2percent:.2f}%")
print(f"{p3percent:.2f}%")
print(f"{p4percent:.2f}%")
print(f"{p5percent:.2f}%")
