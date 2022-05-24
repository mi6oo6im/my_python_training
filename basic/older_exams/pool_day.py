import math

number_of_people = int(input())
entry_tax = float(input())
sun_bed_price = float(input())
sun_umbrella_price = float(input())

sun_bed_number = math.ceil(number_of_people * 0.75)
sun_umbrella_number = math.ceil(number_of_people * 0.5)

sun_bed_cost = sun_bed_number * sun_bed_price
sun_umbrella_cost = sun_umbrella_number * sun_umbrella_price
entry_cost = number_of_people * entry_tax

total_price = entry_cost + sun_bed_cost + sun_umbrella_cost
print(f"{total_price:.2f} lv.")
