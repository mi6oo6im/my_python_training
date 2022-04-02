import math

tournaments = int(input())
starting_points = int(input())
points_won = 0
average_points = 0
tournaments_won = 0
percentage_won = 0


for i in range(tournaments):
    staging = input()
    if staging == "W":
        tournaments_won += 1
        points_won += 2000
    elif staging == "F":
        points_won += 1200
    elif staging == "SF":
        points_won += 720

final_points = starting_points + points_won
average_points = math.floor(points_won / tournaments)
percentage_won = tournaments_won / tournaments * 100

# outputs
print(f"Final points: {final_points}")
print(f"Average points: {average_points:.0f}")
print(f"{percentage_won:.2f}%")
