def dictionary(stock: list, stock_dictionary: dict):
    for i in range(0, len(stock), 2):
        key = stock[i]
        value = int(stock[i + 1])
        stock_dictionary[key] = value
    return stock_dictionary


def stock_check(stock: dict, product: str):
    if product in stock.keys() and stock[product] > 0:
        print(f'We have {stock[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")


stock_list = input().split()
stock_dict = {}
stock_dict = dictionary(stock_list, stock_dict)
products_list = input().split()
for prod in products_list:
    stock_check(stock_dict, prod)
