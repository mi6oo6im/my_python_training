import re

regex = r"w{3}\.[a-zA-Z\-0-9]+(\.[a-z]+)+"
text = input()
res = ''
while len(text) > 0:
    matches = re.finditer(regex, text)
    for match in matches:
        res = match.group(0)
        print(res)
    text = input()

