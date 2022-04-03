minutes_per_walk = int(input())
walks_daily = int(input())
calories_daily = int(input())
calories_per_minute = 5


calories_burned = minutes_per_walk * walks_daily * calories_per_minute

if calories_burned > calories_daily:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")
