input_line = input()
products = {}
while input_line != 'statistics':
    key, value = input_line.split(': ')
    if key in products:
        products[key] += int(value)
    else:
        products[key] = int(value)
    input_line = input()
products_sum = sum(products.values())
products_qty = len(products)
products_list = []
for prod, value in products.items():
    products_list.append(f'- {prod}: {value}')
product_string = '\n'.join(products_list)
print(f'Products in stock:\n{product_string}\nTotal Products: {products_qty}\nTotal Quantity: {products_sum}')