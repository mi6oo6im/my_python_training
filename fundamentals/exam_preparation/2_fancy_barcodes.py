import re


def is_valid_func(_barcode: str, _pattern: str):
    matches = re.match(_pattern, _barcode)
    if matches:
        return True
    else:
        return False


def product_group_func(_barcode: str, _pattern):
    match = re.match(_pattern, _barcode)
    product = match.group('product')
    _product_group = ''
    for symbol in product:
        if symbol.isdigit():
            _product_group += symbol
    if _product_group:
        return _product_group
    else:
        return '00'


number_of_barcodes = int(input())
product_group = ''
valid_barcode_pattern = r'(@#+)(?P<product>[A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)'
for _ in range(number_of_barcodes):
    barcode = input()
    if is_valid_func(barcode, valid_barcode_pattern):
        product_group = product_group_func(barcode, valid_barcode_pattern)
        print(f'Product group: {product_group}')
    else:
        print("Invalid barcode")
