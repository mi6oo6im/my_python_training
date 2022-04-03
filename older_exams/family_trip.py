vacation_budget = float(input())
number_nights = int(input())
cost_per_night = float(input())
extra_cost_percent = int(input())

if number_nights > 7:
    cost_per_night *= 0.95

total_cost = (number_nights * cost_per_night) + vacation_budget * extra_cost_percent / 100

difference = abs(total_cost - vacation_budget)

if vacation_budget >= total_cost:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")
