import re


def extract_pattern(regex, text):
    res = []
    matches = re.findall(regex, text)
    for match in matches:
        res.append(match)
    return res


text = input()
regex = r'\d+'
res = []
while len(text) > 0:
    res += extract_pattern(regex, text)
    text = input()
print(*res, sep=' ')
