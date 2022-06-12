def negative_or_positive(number: int):
    if number < 0:
        return 'negative'
    else:
        return 'positive'


def multiplication_sign(first: int, second: int, third: int):
    numbers_list = [first, second, third]
    if 0 in numbers_list:
        return 'zero'
    positive_negative_list = list(map(negative_or_positive, numbers_list))
    negative_numbers = positive_negative_list.count('negative')
    if negative_numbers % 2 != 0:
        return 'negative'
    else:
        return 'positive'


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(multiplication_sign(first_number, second_number, third_number))
