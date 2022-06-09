def order(product, quantity):
    dictionary = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00
    }
    return f"{dictionary[product] * quantity:.2f}"


prod = input()
qty = int(input())
print(order(prod, qty))