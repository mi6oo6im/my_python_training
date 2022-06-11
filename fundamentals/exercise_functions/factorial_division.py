def factorial(number: int):
    result = number
    for digit in range(1, number):
        result *= digit
    return result


first_number = int(input())
second_number = int(input())

print(f'{factorial(first_number) / factorial(second_number):.2f}')
