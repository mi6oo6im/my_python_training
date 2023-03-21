# def number_increment(numbers):
#
#     def increase():
#
#         return [x + 1 for x in numbers]
#
#     return increase()
#
#
# print(number_increment([1, 2, 3]))

def my_decorator(func):
    def wrapper(numbers):
        numbers = [x + 1 for x in numbers]
        return func(numbers)

    return wrapper


@my_decorator
def number_increment(numbers):
    return numbers
