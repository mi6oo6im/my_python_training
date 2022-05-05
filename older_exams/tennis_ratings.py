import math

tournaments = int(input())
initial_points = int(input())


total_points = initial_points
average_points = 0
percent_won_tournament = 0

for tournament in range(tournaments):
    stage_of_tournament = input()
    if stage_of_tournament == "W":
        total_points += 2000
        percent_won_tournament += 1
    elif stage_of_tournament == "F":
        total_points += 1200
    else:
        total_points += 720

average_points = (total_points-initial_points) / tournaments
percent_won_tournament = percent_won_tournament / tournaments * 100
print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percent_won_tournament:.2f}%")
