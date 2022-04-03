points = {"W": 3, "D": 1, "L": 0}
team_name = input()
points_won = 0
games_won = 0
games_drawn = 0
games_lost = 0
percent_won_game = 0
games_played = int(input())
total_games_played = 0

for game in range(games_played):
    game_outcome = input()
    points_won += points[game_outcome]
    total_games_played += 1
    if game_outcome == "W":
        games_won += 1
    elif game_outcome == "D":
        games_drawn += 1
    else:
        games_lost += 1

if games_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    percent_won_game = games_won / total_games_played * 100
    print(f"{team_name} has won {points_won} points during this season.")
    print(f"Total stats:")
    print(f"## W: {games_won}")
    print(f"## D: {games_drawn}")
    print(f"## L: {games_lost}")
    print(f"Win rate: {percent_won_game:.2f}%")
