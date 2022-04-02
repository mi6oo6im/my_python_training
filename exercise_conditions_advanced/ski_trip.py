room_rates = {
    "room for one person": 18.0,
    "apartment": 25.0,
    "president apartment": 35.0
}

days = int(input())
room_type = input()
csat = input()

total_cost = 0

total_cost = (days-1) * room_rates[room_type]

if days < 10:
    if room_type == "apartment":
        total_cost *= 0.7
    elif room_type == "president apartment":
        total_cost *= 0.9
elif days <= 15:
    if room_type == "apartment":
        total_cost *= 0.65
    elif room_type == "president apartment":
        total_cost *= 0.85
else:
    if room_type == "apartment":
        total_cost *= 0.5
    elif room_type == "president apartment":
        total_cost *= 0.80

if csat == "positive":
    total_cost *= 1.25
else:
    total_cost *= 0.9

# output
print(f"{total_cost:.2f}")
