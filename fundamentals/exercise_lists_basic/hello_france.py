ticket_cost = 150
max_price_dictionary = {
    'Clothes': 50.00,
    'Shoes': 35.00,
    'Accessories': 20.50
}
new_prices_list = []
bought_items_price_list = []
items_list = input().split('|')
budget = float(input())
for item in items_list:
    current_item_list = item.split('->')
    current_item = current_item_list[0]
    item_price = float(current_item_list[1])
    if item_price <= max_price_dictionary[current_item] and budget >= item_price:
        budget -= item_price
        new_price = item_price * 1.40
        new_prices_list.append(new_price)
        bought_items_price_list.append(item_price)
total_cost = sum(bought_items_price_list)
total_income = sum(new_prices_list)
new_price_string_list = [f'{x:.2f}' for x in new_prices_list]
new_price_string = ' '.join(new_price_string_list)
profit = total_income - total_cost
print(new_price_string)
print(f'Profit: {profit:.2f}')
money_in_hand = budget + total_income
if money_in_hand >= ticket_cost:
    print('Hello, France!')
else:
    print('Not enough money.')
