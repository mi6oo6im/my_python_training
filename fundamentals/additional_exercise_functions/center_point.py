import math


def closer_point(x1: float, y1: float, x2: float, y2: float):
    point1 = f'({math.floor(x1)}, {math.floor(y1)})'
    point2 = f'({math.floor(x2)}, {math.floor(y2)})'
    r1 = (x1 ** 2 + y1 ** 2) ** (1 / 2)
    r2 = (x2 ** 2 + y2 ** 2) ** (1 / 2)
    if r1 <= r2:
        return point1
    else:
        return point2


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(closer_point(x1, y1, x2, y2))
