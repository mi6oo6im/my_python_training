# inputs
years_old = int(input())
washing_machine_price = float(input())
toy_price = int(input())

# calculation variables
toy_number = 0
total_money = 0
annual_money = 0
brother_tax = 0

for i in range(1, years_old + 1):
    if i % 2 == 0:
        annual_money += 10
        total_money += annual_money
        brother_tax += 1
    else:
        toy_number += 1

toy_income = toy_number * toy_price

budget = toy_income + total_money - brother_tax

difference = abs(budget - washing_machine_price)

if budget >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
