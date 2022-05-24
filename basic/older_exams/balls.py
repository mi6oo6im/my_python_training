import math

number_of_balls = int(input())
total_points = 0
red_balls = 0
yellow_balls = 0
orange_balls = 0
white_balls = 0
black_balls = 0
other_balls = 0

for ball in range(number_of_balls):
    color = input()
    if color == "red":
        total_points += 5
        red_balls += 1
    elif color == "orange":
        total_points += 10
        orange_balls += 1
    elif color == "yellow":
        total_points += 15
        yellow_balls += 1
    elif color == "white":
        total_points += 20
        white_balls += 1
    elif color == "black":
        total_points = math.floor(total_points / 2)
        black_balls += 1

other_balls = number_of_balls - (red_balls + orange_balls + yellow_balls + white_balls + black_balls)

print(f"Total points: {total_points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_balls}")
