def bus_tour(cities: int):
    total_income = 0
    total_cost = 0
    for city in range(1, cities + 1):
        city_name = input()
        current_income = float(input())
        current_cost = float(input())
        if city % 3 == 0 and city % 5 != 0:
            current_cost *= 1.5  # 50% over the cost due to special event
        if city % 5 == 0:
            current_income *= 0.9  # -10% of income due to bad weather
        total_cost += current_cost
        total_income += current_income
        current_profit = current_income - current_cost
        print(f'In {city_name} Burger Bus earned {current_profit:.2f} leva.')
    total_profit = total_income - total_cost
    print(f'Burger Bus total profit: {total_profit:.2f} leva.')


number_of_cities = int(input())
bus_tour(number_of_cities)
