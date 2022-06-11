def is_even(number: str):
    if int(number) % 2 == 0:
        return True


def even_numbers_only(number_string: list):
    list_even_numbers_strings = list(filter(is_even, number_string))
    return list(int(x) for x in list_even_numbers_strings)


single_number_list = input().split()
print(even_numbers_only(single_number_list))