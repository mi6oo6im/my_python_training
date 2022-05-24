import sys
best_player = ''
player = input()
hat_trick = False
top_goals = -sys.maxsize
while player != "END":
    goals = int(input())
    if goals > top_goals:
        top_goals = goals
        best_player = player
    if goals >= 3:
        hat_trick = True
    if goals >= 10:
        break
    player = input()

print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {top_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {top_goals} goals.")
