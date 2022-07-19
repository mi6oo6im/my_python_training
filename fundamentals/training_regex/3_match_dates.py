import re

dates = input()
regex = r'(\d{2})(\/|-|\.)([A-Z][a-z]{2})(\2)(\d{4})'
matches = re.finditer(regex, dates)
date_list = []
for match in matches:
    day = match.group(1)
    month = match.group(3)
    year = match.group(5)
    date = f'Day: {day}, Month: {month}, Year: {year}'
    date_list.append(date)

print(*date_list, sep='\n')
