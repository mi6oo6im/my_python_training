def func_executor(*args):
    functions = args
    results = []
    for func in functions:
        results.append(f'{func[0].__name__} - {func[0](*func[1])}')

    result = '\n'.join(map(str, results))
    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
