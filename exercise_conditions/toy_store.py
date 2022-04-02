# Цени на играчките:
# #  Пъзел - 2.60 лв.
# #  Говореща кукла - 3 лв.
# #  Плюшено мече - 4.10 лв.
# #  Миньон - 8.20 лв.
# #  Камионче - 2 лв.
# # Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена. От спечелените
# # пари Петя трябва да даде 10% за наема на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на
# # екскурзия.

# prices variables
jigsaw_price = 2.6
talking_doll_price = 3
teddy_bear_price = 4.1
minion_price = 8.2
truck_price = 2

# input variables
trip_price = float(input())
num_jigsaw = int(input())
num_doll = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

# calculation variables
jigsaw_income = num_jigsaw * jigsaw_price
doll_income = num_doll * talking_doll_price
bear_income = num_bears * teddy_bear_price
minion_income = num_minions * minion_price
truck_income = num_trucks * truck_price

total_income = jigsaw_income + doll_income + bear_income + minion_income + truck_income
total_toys = num_jigsaw + num_doll + num_bears + num_minions + num_trucks

discount = 0

if 50 <= total_toys:
    discount = 0.25 * total_income

revenue = total_income - discount
rent = revenue * 0.1
profit = revenue - rent

# output
if trip_price > profit:
    print(f"Not enough money! {trip_price - profit:.2f} lv needed.")
else:
    print(f"Yes! {profit - trip_price:.2f} lv left.")
