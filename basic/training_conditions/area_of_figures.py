# square a, rectangle a and b, circle r, triangle a and b
from math import pi as pi

figure_type = input()
if figure_type == 'square':
    a = float(input())
    print(f"{pow(a, 2):.3f}")
elif figure_type == 'rectangle':
    a = float(input())
    b = float(input())
    print(f"{a * b:.3f}")
elif figure_type == 'circle':
    r = float(input())
    print(f"{pi * pow(r, 2):.3f}")
elif figure_type == 'triangle':
    a = float(input())
    b = float(input())
    print(f"{a * b / 2:.3f}")
