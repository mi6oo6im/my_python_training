def minimum_num(numbers_list: list):
    return min(numbers_list)


def maximum_num(numbers_list: list):
    return max(numbers_list)


def sum_all_numbers(numbers_list: list):
    return sum(numbers_list)


def min_max_sum_print(numbers_list: list):
    minimum_number = minimum_num(numbers_list)
    maximum_number = maximum_num(numbers_list)
    sum_of_number = sum_all_numbers(numbers_list)
    print(f"The minimum number is {minimum_number}")
    print(f"The maximum number is {maximum_number}")
    print(f"The sum number is: {sum_of_number}")


list_of_numbers_string = list(int(x) for x in input().split())
min_max_sum_print(list_of_numbers_string)
