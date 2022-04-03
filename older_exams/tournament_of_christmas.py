tournament_days = int(input())
charity_money = 0
day_wins = 0
tournament_is_won = False
for day in range(tournament_days):
    charity_money_day = 0
    wins = 0
    loses = 0
    sport = input()
    while sport != "Finish":
        result = input()
        if result == "win":
            charity_money_day += 20
            wins += 1
        else:
            loses += 1
        sport = input()
    if wins > loses:
        charity_money += charity_money_day * 1.1
        day_wins += 1
    else:
        charity_money += charity_money_day

if day_wins > tournament_days - day_wins:
    charity_money *= 1.2
    tournament_is_won = True

if tournament_is_won:
    print(f"You won the tournament! Total raised money: {charity_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {charity_money:.2f}")
