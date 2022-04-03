player_1_eggs = int(input())
player_2_eggs = int(input())

while player_1_eggs != 0 and player_2_eggs != 0:
    command = input()
    if command == "one":
        player_2_eggs -= 1
    elif command == "two":
        player_1_eggs -= 1
    elif command == "End of battle":
        break

if player_1_eggs == 0:
    print(f"Player one is out of eggs. Player two has {player_2_eggs} eggs left.")
elif player_2_eggs == 0:
    print(f"Player two is out of eggs. Player one has {player_1_eggs} eggs left.")
else:
    print(f"Player one has {player_1_eggs} eggs left.")
    print(f"Player two has {player_2_eggs} eggs left.")
