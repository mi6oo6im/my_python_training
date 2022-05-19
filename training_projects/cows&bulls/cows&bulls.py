import random

# computer's generated 4-digit number
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
random.shuffle(num_list)
number_to_guess = []
for _ in range(4):
    number_to_guess.append(num_list.pop(0))
number_to_guess_string = ''.join(number_to_guess)
print(number_to_guess_string)
cows = 0;
bulls = 0;
# input
guess_list =[]
guess = input('Make your guess: ')
guess_list.append(guess)
if guess == number_to_guess_string:
    print('You win!')
else:
    for i, j in enumerate(guess):
        if j == number_to_guess[i]:
            bulls += 1
        elif j in number_to_guess:
            cows += 1
    print('Try again!')
    print(f'cows: {cows}; bulls: {bulls}')
    print(f'your guesses so far: {guess_list}')
