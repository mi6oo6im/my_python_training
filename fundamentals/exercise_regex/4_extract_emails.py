import re

text = input()
regex = r"((?<= )[a-z0-9]+)([\._-]?)([a-z0-9]*)@([a-z]+-?[a-z]*)(\.[a-z]+-?[a-z]*)+\b"
matches = re.finditer(regex, text)
res = [x.group(0) for x in matches]
print(*res, sep='\n')
