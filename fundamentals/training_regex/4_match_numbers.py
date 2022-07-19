import re

numbers = input()
regex = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+|)($|(?=\s))'
matches = re.finditer(regex, numbers)
numbers_list = []
for match in matches:
    numbers_list.append(match.group(0))
print(*numbers_list, sep=' ')
