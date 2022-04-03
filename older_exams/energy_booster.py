# "Watermelon", "Mango", "Pineapple" или "Raspberry"

small_pack = {
    "Watermelon": 56,
    "Mango": 36.66,
    "Pineapple": 42.10,
    "Raspberry": 20
}
big_pack = {
    "Watermelon": 28.70,
    "Mango": 19.60,
    "Pineapple": 24.80,
    "Raspberry": 15.20
}

fruit = input()
pack_size = input()
set_num = int(input())
discount = 0
total_price = 0

if pack_size == "small":
    total_price = set_num * 2 * small_pack[fruit]
else:
    total_price = set_num * 5 * big_pack[fruit]

if 400 <= total_price <= 1000:
    discount = 0.15 * total_price
elif total_price > 1000:
    discount = 0.5 * total_price
final_price = total_price - discount
print(f"{final_price:.2f} lv.")

