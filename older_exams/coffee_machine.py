# "Espresso", "Cappuccino" или "Tea"
# "Without", "Normal" или "Extra"

dictionary = {"EspressoWithout": 0.90,
              "EspressoNormal": 1.0,
              "EspressoExtra": 1.20,
              "CappuccinoWithout": 1.00,
              "CappuccinoNormal": 1.20,
              "CappuccinoExtra": 1.60,
              "TeaWithout": 0.50,
              "TeaNormal": 0.60,
              "TeaExtra": 0.70}

drink = input()
sugar = input()
number_of_drinks = int(input())

cost = number_of_drinks * dictionary[drink+sugar]

if sugar == "Without":
    cost *= 0.65
if drink == "Espresso" and number_of_drinks >= 5:
    cost *= 0.75
if cost > 15:
    cost *= 0.8

print(f"You bought {number_of_drinks} cups of {drink} for {cost:.2f} lv.")
