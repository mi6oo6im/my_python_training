import random
# the rules
print("\nBulls and Cows is a logic game for guessing numbers. It is played by two opponents, each trying to guess the secret 4-digit number invented by the other.\nAfter each move, the opponent gives the number of matches.")
print("The game is played until you guess correctly the opponent's number or until you type 'Uncle!' in the console.")
print("if a digit of the guess is contained in the secret number and is in the right place, it is 'bull', if it is in a different place, it is 'cow'.\n")
# computer's generated 4-digit number
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
random.shuffle(num_list)
number_to_guess = []
for _ in range(4):
    number_to_guess.append(num_list.pop(0))
number_to_guess_string = ''.join(number_to_guess)
# print(number_to_guess_string)
cows = 0
bulls = 0
# input
guess_list = []
guess = input('Make your 4-digit number guess or cry "Uncle!": ')
is_chicken = True
while guess != 'Uncle!':
    guess_list.append(guess)
    if guess == number_to_guess_string:
        print(f'You win! {guess} is the correct number!')
        is_chicken = False
        break
    else:
        for i, j in enumerate(guess):
            if j == number_to_guess[i]:
                bulls += 1
            elif j in number_to_guess:
                cows += 1
        print('Try again or cry "Uncle!"\n')
        print(f'cows: {cows}; bulls: {bulls}')
        print(f'your guesses so far: {guess_list} \n')
    guess = input('Make your guess or cry "Uncle!": ')
if is_chicken:
    print('You chickened out!')
