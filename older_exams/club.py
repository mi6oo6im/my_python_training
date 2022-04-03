targeted_gain = float(input())
cocktail_name = input()
total_gained = 0
target_acquired = False
while cocktail_name != "Party!":
    number_of_cocktails = int(input())
    order_price = number_of_cocktails * len(cocktail_name)
    if order_price % 2 != 0:
        order_price *= 0.75
    total_gained += order_price
    if total_gained >= targeted_gain:
        target_acquired = True
        break
    cocktail_name = input()

if target_acquired:
    print("Target acquired.")
else:
    difference = abs(targeted_gain - total_gained)
    print(f"We need {difference:.2f} leva more.")

print(f"Club income - {total_gained:.2f} leva.")
