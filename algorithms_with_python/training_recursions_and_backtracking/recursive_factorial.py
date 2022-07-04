def factorial_recursion(number: int):
    if number == 0:
        return 1
    return number * factorial_recursion(number - 1)


factorial_num = int(input())
print(factorial_recursion(factorial_num))
