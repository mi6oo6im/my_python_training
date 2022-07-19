import re
numbers = input()
regex = r'\+359( |-)2(\1)\d{3}(\1)\d{4}\b'
matches = re.finditer(regex, numbers)
res = []
for match in matches:
    match_str = match.group(0)
    res.append(match_str)
print(*res, sep=', ')
