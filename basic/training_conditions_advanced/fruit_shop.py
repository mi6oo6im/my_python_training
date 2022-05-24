fruit = input()
weekday = input()
qty = float(input())

price = 0

is_workday = weekday in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
is_weekend = weekday in ("Saturday", "Sunday")
is_fruit = fruit in ("banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes")

workday_prices = {
    "banana": 2.50,
    "apple": 1.20,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85
}

weekend_prices = {
    "banana": 2.70,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20
}

if is_workday and is_fruit:
    price = workday_prices[fruit]
elif is_weekend and is_fruit:
    price = weekend_prices[fruit]

total_price = price * qty
if total_price != 0:
    print(f"{total_price:.2f}")
else:
    print("error")
