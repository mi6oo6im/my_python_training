seasons = ["Spring", "Summer", "Autumn", "Winter"]

seasons_rent = {"Spring": 3000,
                "Summer": 4200,
                "Autumn": 4200,
                "Winter": 2600}

budget = int(input())
season = input()
fishermen = int(input())
discount = 0
difference = 0

if fishermen <= 6:
    discount = 0.1
elif fishermen <= 11:
    discount = 0.15
elif fishermen >= 12:
    discount = 0.25

total_cost = seasons_rent[season] - seasons_rent[season] * discount

if fishermen % 2 == 0 and season != "Autumn":
    total_cost -= total_cost * 0.05

difference = abs(budget - total_cost)
# output
if budget >= total_cost:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")

# Not enough money! You need 180.00 leva.
# Not enough money! You need 180.00 leva.
# Yes! You have 50.00 leva left.
# Yes! You have 50.00 leva left.
