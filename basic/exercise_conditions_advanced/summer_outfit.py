degree = int(input())
time_of_day = input()

outfit = ''
shoes = ''
combo = 0

all_outfits = ["Sweatshirt", "Shirt", "T-Shirt", "Swim Suit"]
all_shoes = ["Sneakers", "Moccasins", "Sandals", "Barefoot"]

if time_of_day == "Evening":
    combo = 1
elif time_of_day == "Morning":
    if 10 <= degree <= 18:
        combo = 0
    elif 18 < degree <= 24:
        combo = 1
    elif degree >= 25:
        combo = 2
elif time_of_day == "Afternoon":
    if 10 <= degree <= 18:
        combo = 1
    elif 18 < degree <= 24:
        combo = 2
    elif degree >= 25:
        combo = 3

outfit = all_outfits[combo]
shoes = all_shoes[combo]

print(f"It's {degree} degrees, get your {outfit} and {shoes}.")
