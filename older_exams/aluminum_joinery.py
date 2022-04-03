# "90X130" или "100X150" или "130X180" или "200X300";
prices = {"90X130": 110, "100X150": 140, "130X180": 190, "200X300": 250}

num_joins = int(input())
profile = input()
delivery = input()

single_price = prices[profile]

total_price = num_joins * single_price

discount = 0

if profile == "90X130":
    if 30 < num_joins <= 60:
        discount = 5
    elif num_joins > 60:
        discount = 8
elif profile == "100X150":
    if 40 < num_joins <= 80:
        discount = 6
    elif num_joins > 80:
        discount = 10
if profile == "130X180":
    if 20 < num_joins <= 50:
        discount = 7
    elif num_joins > 50:
        discount = 12
if profile == "200X300":
    if 25 < num_joins <= 50:
        discount = 9
    elif num_joins > 50:
        discount = 14

final_price = total_price * (1 - discount / 100)

if delivery == "With delivery":
    final_price += 60

if num_joins > 99:
    final_price *= 0.96

if num_joins < 10:
    print("Invalid order")
else:
    print(f"{final_price:.2f} BGN")
