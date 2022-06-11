def sum_numbers(first_number: int, second_number: int):
    return first_number + second_number


def subtract_numbers(sum: int, third_number: int):
    return sum - third_number


def add_and_subtract(first_number: int, second_number: int, third_number: int):
    sum_of_numbers = sum_numbers(first_number, second_number)
    result = subtract_numbers(sum_of_numbers, third_number)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
