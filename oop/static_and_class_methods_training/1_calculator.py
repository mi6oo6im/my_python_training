from functools import reduce
from typing import List


class Calculator:

    @staticmethod
    def add(*args: int) -> int:
        num_list = args
        result = sum(num_list)
        return result

    @staticmethod
    def multiply(*args: int) -> int:
        num_list = args
        result = reduce(lambda a, b: a * b, num_list)
        return result

    @staticmethod
    def divide(*args: int) -> float:
        num_list = args
        result = reduce(lambda a, b: a / b, num_list)
        return result

    @staticmethod
    def subtract(*args: int) -> int:
        num_list = args
        result = reduce(lambda a, b: a - b, num_list)
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
