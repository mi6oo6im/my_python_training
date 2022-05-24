bag_price_above_20kg = float(input())
luggage_kilograms = float(input())
travel_days = int(input())
number_of_bags = int(input())
luggage_price = 0
if luggage_kilograms < 10:
    luggage_price = 0.2 * bag_price_above_20kg
elif luggage_kilograms <= 20:
    luggage_price = 0.5 * bag_price_above_20kg
else:
    luggage_price = bag_price_above_20kg

total_price = luggage_price * number_of_bags

if travel_days < 7:
    total_price *= 1.4
elif travel_days <= 30:
    total_price *= 1.15
else:
    total_price *= 1.1

print(f"The total price of bags is: {total_price:.2f} lv.")
