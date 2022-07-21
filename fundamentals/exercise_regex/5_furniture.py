import re

regex = r">>(?P<name>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"
furniture_data = input()
total_cost = 0
furniture_list = []
while furniture_data != 'Purchase':
    matches = re.finditer(regex, furniture_data, re.MULTILINE)
    for match in matches:
        furniture = match.group('name')
        price = float(match.group('price'))
        qty = int(match.group('quantity'))
        cost = price * qty
        total_cost += cost
        furniture_list.append(furniture)
    furniture_data = input()

print('Bought furniture:')
if furniture_list:
    print(*furniture_list, sep='\n')
print(f'Total money spend: {total_cost:.2f}')
