budget = float(input())
destination = input()  # "Dubai", "Sofia", "London"
season = input()  # "Summer", "Winter"
days_vacation = int(input())

dictionary = {
    "DubaiSummer": 40000,
    "SofiaSummer": 12500,
    "LondonSummer": 20250,
    "DubaiWinter": 45000,
    "SofiaWinter": 17000,
    "LondonWinter": 24000
}
price_per_day = dictionary[destination+season]
total_cost = price_per_day * days_vacation
if destination == "Dubai":
    total_cost *= 0.70
elif destination == "Sofia":
    total_cost *= 1.25

difference = abs(total_cost - budget)

if budget >= total_cost:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")
