import re

text = input()
word_to_count = input()
regex = rf'\b{word_to_count}\b'
matches = re.findall(regex, text, re.IGNORECASE)
print(len(matches))
