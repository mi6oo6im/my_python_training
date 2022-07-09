input_line = input()
products_dict = {}
while input_line != 'buy':
    product, price, quantity = input_line.split()
    if product not in products_dict.keys():
        products_dict[product] = [float(price), int(quantity)]
    else:
        products_dict[product][0] = float(price)
        products_dict[product][1] += int(quantity)
    input_line = input()

for k, v in products_dict.items():
    product = k
    price = v[0]
    quantity = v[1]
    print(f'{product} -> {price * quantity:.2f}')
