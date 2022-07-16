def get_letter_position(letter: str):
    return ord(letter.lower()) - 96


def divide_func(number: int, letter_position: int):
    return number / letter_position


def multiply_func(number: int, letter_position: int):
    return number * letter_position


def subtract_func(number: int, letter_position: int):
    return number - letter_position


def add_func(number: int, letter_position: int):
    return number + letter_position


string_list = input().split()
total_sum = 0

for string in string_list:
    current_num = int(''.join([x for x in string if x.isnumeric()]))
    first_letter = string[0]
    second_letter = string[-1]
    if first_letter.isupper():
        current_num = divide_func(current_num, get_letter_position(first_letter))
    else:
        current_num = multiply_func(current_num, get_letter_position(first_letter))
    if second_letter.isupper():
        current_num = subtract_func(current_num, get_letter_position(second_letter))
    else:
        current_num = add_func(current_num, get_letter_position(second_letter))
    total_sum += current_num
print(f'{total_sum:.2f}')
