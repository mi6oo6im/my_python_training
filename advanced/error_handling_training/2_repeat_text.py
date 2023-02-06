# import sys
# from io import StringIO
#
# test_input = '''Hello SoftUni
# 3'''
#
# sys.stdin = StringIO(test_input)


def text_repeater(txt, times):
    return txt * times


try:
    text = input('Please enter text string: ')
    nums = int(input('Please enter a valid integer: '))
    print(text_repeater(text, nums))
except ValueError:
    print('Variable times must be an integer')
