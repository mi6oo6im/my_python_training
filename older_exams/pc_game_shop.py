number_games_sold = int(input())
Hearthstone = 0
Fornite = 0
Overwatch = 0
Others = 0

for game in range (number_games_sold):
    title = input()
    if title == "Hearthstone":
        Hearthstone += 1
    elif title == "Fornite":
        Fornite += 1
    elif title == "Overwatch":
        Overwatch += 1
    else:
        Others += 1

Hearthstone_percent = round(Hearthstone / number_games_sold * 100, 2)
Fornite_percent = round(Fornite / number_games_sold * 100, 2)
Overwatch_percent = round(Overwatch / number_games_sold * 100, 2)
Others_percent = round(Others / number_games_sold * 100, 2)


print(f"Hearthstone - {Hearthstone_percent:.2f}%")
print(f"Fornite - {Fornite_percent:.2f}%")
print(f"Overwatch - {Overwatch_percent:.2f}%")
print(f"Others - {Others_percent:.2f}%")
