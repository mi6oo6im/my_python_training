import sys

command = input()
top_score = -sys.maxsize
winner = ""
win_flag = 0
while command != "Stop":
    player = command
    player_score = 0
    for letter in player:
        guess_num = int(input())
        ascii_letter = ord(letter)
        if ascii_letter == guess_num:
            player_score += 10
        else:
            player_score += 2
    if top_score < player_score:
        winner = player
        top_score = player_score
    elif top_score == player_score:
        win_flag += 1
        if win_flag == 1:
            winner = player
            top_score = player_score
    command = input()
if top_score > 0:
    print(f"The winner is {winner} with {top_score} points!")
