import math


def longer_line(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float):
    d1 = pow((pow((x2 - x1), 2) + pow((y2 - y1), 2)), (1 / 2))
    d2 = pow((pow((x4 - x3), 2) + pow((y4 - y3), 2)), (1 / 2))
    if d1 >= d2:
        line_points = closer_point(x1, y1, x2, y2)
    else:
        line_points = closer_point(x3, y3, x4, y4)
    return line_points


def closer_point(x1: float, y1: float, x2: float, y2: float):
    point1 = f'({math.floor(x1)}, {math.floor(y1)})'
    point2 = f'({math.floor(x2)}, {math.floor(y2)})'
    r1 = (x1 ** 2 + y1 ** 2) ** (1 / 2)
    r2 = (x2 ** 2 + y2 ** 2) ** (1 / 2)
    if r1 <= r2:
        return f'{point1}{point2}'
    else:
        return f'{point2}{point1}'


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(longer_line(x1, y1, x2, y2, x3, y3, x4, y4))
