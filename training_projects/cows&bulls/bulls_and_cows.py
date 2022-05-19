import random

# the rules
print(
    "\nBulls and Cows is a logic game for guessing numbers. It is played by two opponents, each trying to guess the secret 4-digit number (without repeating digit) invented by the other.\nAfter each move, the opponent gives the number of matches.")
print("The game is played until you guess correctly the opponent's number or until you type 'Uncle!' in the console.")
print(
    "If a digit of the guess is contained in the secret number and is in the right place, it is 'bull', if it is in a different place, it is 'cow'.\n")
# computer's generated 4-digit number
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
random.shuffle(num_list)
while num_list[0] == '0':
    random.shuffle(num_list)
number_to_guess = []
for _ in range(4):
    number_to_guess.append(num_list.pop(0))
number_to_guess_string = ''.join(number_to_guess)
# print(number_to_guess_string)
# input
guess_list = []
guess = input('Make your 4-digit number guess or cry "Uncle!": ')
is_chicken = True
counter = 0
while guess != 'Uncle!':
    number_is_wrong = False
    new_guess_list = list(guess)
    for _ in range(4):
        check = new_guess_list.pop(0)
        if check in new_guess_list or guess[0] == '0' or len(guess) != 4 or guess.isdigit() != True:
            print(
                f'The number you have entered {guess} has repeating digits,starts with 0 or is not a 4-digit number, please try again!\n')
            guess = input('Make your guess or cry "Uncle!": ')
            number_is_wrong = True
            break
    if number_is_wrong:
        continue
    counter += 1
    cows = 0
    bulls = 0
    guess_list.append(guess)
    if guess == number_to_guess_string:
        print(f'You win! {guess} is the correct number after {counter} attempts!')
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
    print(f'You chickened out after {counter} attempts!')
