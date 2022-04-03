import sys

command = input()
player = ""
winner = ""
top_score = -sys.maxsize
guess_num = 0
flag = 0
while command != "Stop":
    player = command
    current_score = 0
    for letter in command:
        guess_num = int(input())
        if ord(letter) == guess_num:
            current_score += 10
        else:
            current_score += 2
    if current_score > top_score:
        top_score = current_score
        winner = player
        flag = 0
    elif current_score == top_score and flag == 0:
        flag = 1
        top_score = current_score
        winner = player

    command = input()


print(f"The winner is {winner} with {top_score} points!")
