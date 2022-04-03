# Gym	Boxing	Yoga	Zumba	Dances	Pilates

m_prices = {"Gym": 42,
            "Boxing": 41,
            "Yoga": 45,
            "Zumba": 34,
            "Dances": 51,
            "Pilates": 39
            }
f_prices = {"Gym": 35,
            "Boxing": 37,
            "Yoga": 42,
            "Zumba": 31,
            "Dances": 53,
            "Pilates": 37
            }
budget = float(input())
gender = input()
age = int(input())
sport = input()
price = 0
discount = 0
if gender == "m":
    price = m_prices[sport]
else:
    price = f_prices[sport]

if age <= 19:
    discount = price * 0.2

total_price = price - discount

if total_price <= budget:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    difference = abs(total_price - budget)
    print(f"You don't have enough money! You need ${difference:.2f} more.")
