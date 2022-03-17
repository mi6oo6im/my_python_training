# дали предвидените средства са достатъчни за снимането на филма.
# За снимките ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
#  Декорът за филма е на стойност 10% от бюджета.
#  При повече от 150 статиста, има отстъпка за облеклото на стойност 10%.

# input variables
budget = float(input())
number_of_statists = int(input())
one_dress_price = float(input())

# calculation variables
decor = budget * 0.1

dresses_price = one_dress_price * number_of_statists

if number_of_statists > 150:
    dresses_price *= 0.9

needed_money = decor + dresses_price
abs_diff = abs(budget - needed_money)

if needed_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs_diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs_diff:.2f} leva left.")
