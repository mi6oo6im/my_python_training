import re

regex = r"%(?P<name>[A-Z][a-z]+)%([^|$%.]*?)<(?P<product>\w+)>([^|$%.]*?)\|(?P<quantity>[1-9][0-9]*)\|([^|$%.]*?)(?P<price>[1-9][0-9]*(\.[0-9]{0,2})?)\$"
text = input()
purchase = {}
total_income = 0
while text != 'end of shift':
    matches = re.finditer(regex, text)
    for match in matches:
        name = match.group('name')
        product = match.group('product')
        quantity = match.group('quantity')
        price = match.group('price')
        print(f'{name}: {product} - {int(quantity) * float(price):.2f}')
        total_income += int(quantity) * float(price)
    text = input()

print(f'Total income: {total_income:.2f}')
