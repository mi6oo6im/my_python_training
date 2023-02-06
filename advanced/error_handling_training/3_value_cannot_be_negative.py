import sys
from io import StringIO

test_string = '''1
4
-5
3
10
'''
sys.stdin = StringIO(test_string)


class ValueCannotBeNegative(Exception):
    pass


def negation_check(value):
    if value < 0:
        raise ValueCannotBeNegative(f'---Value cannot be a negative number--- convert {value} to {abs(value)}')
    else:
        return value


numbers = [int(input()) for x in range(5)]

for num in numbers:
    try:
        print(negation_check(num))
    except ValueCannotBeNegative as err:
        print(err)
