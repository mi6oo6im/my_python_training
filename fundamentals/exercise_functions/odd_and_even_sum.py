def is_even(number: str):
    if int(number) % 2 == 0:
        return True


def is_odd(number: str):
    if int(number) % 2 != 0:
        return True


def odd_and_even_sum(number_string: str):
    list_even_numbers = list(filter(is_even, number_string))
    list_odd_numbers = list(filter(is_odd, number_string))
    sum_of_even_digits = sum(list(int(x) for x in list_even_numbers))
    sum_of_odd_digits = sum(list(int(x) for x in list_odd_numbers))
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


single_number = input()
print(odd_and_even_sum(single_number))
