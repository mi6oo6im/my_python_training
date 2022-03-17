seasons = ["summer", "winter"]
destinations = ["Bulgaria", "Balkans", "Europe"]
types = ["Camp", "Hotel"]
seasons = ["summer", "winter"]
vac_type = ""

budget = float(input())
season = input()
spent = 0
destination = ""

if budget <= 100:
    destination = destinations[0]
    if season == seasons[0]:
        spent = budget * 0.3
        vac_type = types[0]
    elif season == seasons[1]:
        spent = budget * 0.7
        vac_type = types[1]
elif budget <= 1000:
    destination = destinations[1]
    if season == seasons[0]:
        spent = budget * 0.4
        vac_type = types[0]
    elif season == seasons[1]:
        spent = budget * 0.8
        vac_type = types[1]
elif budget > 1000:
    destination = destinations[2]
    spent = budget * 0.9
    vac_type = types[1]

# outcome

print(f"Somewhere in {destination}")
print(f"{vac_type} - {spent:.2f}")
