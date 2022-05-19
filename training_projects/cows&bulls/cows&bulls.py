import random
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
random.shuffle(num_list)
number_to_guess = []
for _ in range(4):
    number_to_guess.append(num_list.pop(0))
print(number_to_guess)
print(num_list)
number_to_guess_string = ''.join(number_to_guess)
print(number_to_guess_string)
guess = input('Make your guess: ')
if guess == number_to_guess_string:
    print('You win!')
else:
    print('Try again!')
