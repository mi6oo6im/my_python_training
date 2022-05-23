budget = float(input())
flower_price = float(input())
pack_eggs_price = flower_price * 75 / 100
milk_price = 0.25 * flower_price * (1 + 25 / 100)  # price is for 0.250l
loaf_cost = flower_price + pack_eggs_price + milk_price
number_of_loaves = 0
colored_eggs = 0

while budget > loaf_cost:
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)
        if colored_eggs < 0:
            colored_eggs = 0
    budget -= loaf_cost


print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")