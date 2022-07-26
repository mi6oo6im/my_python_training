import re

food_supply = input()
food_regex = r'([#|\|])(?P<product>[A-z\s]+)\1(?P<date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d{1,5})\1'
matches = re.finditer(food_regex, food_supply)
products_list = []
total_calories = 0
for match in matches:
    product = match.group('product')
    date = match.group('date')
    calories = match.group('calories')
    products_list.append([product, date, int(calories)])
    total_calories += int(calories)
days_to_last = total_calories // 2000
print(f'You have food to last you for: {days_to_last} days!')
[print(f'Item: {x[0]}, Best before: {x[1]}, Nutrition: {x[2]}') for x in products_list]
