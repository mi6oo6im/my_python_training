import re


def is_valid_func(_message: str, _pattern: str):
    match = re.match(_pattern, _message)
    if match:
        return True
    return False


def extract_groups_func(_message: str, _pattern: str):
    match = re.match(_pattern, _message)
    numbers = match.group('numbers')
    lower = match.group('lower')
    upper = match.group('upper')
    symbols = match.group('symbols')
    encrypted = numbers + lower + upper + symbols
    return encrypted


pattern = r'(.+)>(?P<numbers>\d{3})\|(?P<lower>[a-z]{3})\|(?P<upper>[A-Z]{3})\|(?P<symbols>[^<>]{3})<\1'
message_num = int(input())
for _ in range(message_num):
    message = input()
    if is_valid_func(message, pattern):
        print('Password: ', end='')
        print(extract_groups_func(message, pattern))
    else:
        print('Try another password!')
