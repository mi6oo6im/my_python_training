import math

height = int(input())
width = int(input())
percent_excluded = int(input())
area = height * width
total_area_to_cover = math.ceil(area * 4 * (1 - percent_excluded / 100))
walls_are_painted = False
left_paint = 0
command = input()
while command != "Tired!":
    liters = int(command)
    total_area_to_cover -= liters
    if total_area_to_cover <= 0:
        walls_are_painted = True
        left_paint = abs(total_area_to_cover)
        break
    command = input()
else:
    print(f"{total_area_to_cover} quadratic m left.")

if walls_are_painted and left_paint:
    print(f"All walls are painted and you have {left_paint} l paint left!")
elif walls_are_painted and not left_paint:
    print("All walls are painted! Great job, Pesho!")
