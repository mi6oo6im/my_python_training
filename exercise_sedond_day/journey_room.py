month = input()
nights = int(input())

month_cost_ap = {
    "May": 65.0,
    "June": 68.7,
    "July": 77.0,
    "August": 77.0,
    "September": 68.7,
    "October": 65.0
}
month_cost_st = {
    "May": 50.0,
    "June": 75.2,
    "July": 76.0,
    "August": 76.0,
    "September": 75.2,
    "October": 50.0
}

cost_ap = month_cost_ap[month] * nights
cost_st = month_cost_st[month] * nights

if 7 < nights <= 14 and month in ("May", "October"):
    cost_st *= 0.95
elif nights > 14:
    if month in ("May", "October"):
        cost_st *= 0.7
    elif month in ("June", "September"):
        cost_st *= 0.8
    cost_ap *= 0.9

# outputs
print(f"Apartment: {cost_ap:.2f} lv.")
print(f"Studio: {cost_st:.2f} lv.")
