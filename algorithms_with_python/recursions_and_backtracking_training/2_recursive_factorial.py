def factorial_recursion(num):
    if num == 0:
        return 1

    return num * factorial_recursion(num - 1)


print(factorial_recursion(int(input())))
