import re

words = input()
regex = r"\b_[a-zA-Z0-9]+\b"
matches = re.findall(regex, words)
res = [x.replace('_', '') for x in matches]
print(*res, sep=',')