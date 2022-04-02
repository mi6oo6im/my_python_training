# Филм	normal	luxury	ultra luxury
# A Star Is Born	7.50 лв.	10.50 лв.	13.50 лв.
# Bohemian Rhapsody	7.35 лв.	9.45 лв.	12.75 лв.
# Green Book	8.15 лв.	10.25 лв.	13.25 лв.
# The Favourite	8.75 лв.	11.55 лв.	13.95 лв.

normal_prices = {
    "A Star Is Born": 7.5,
    "Bohemian Rhapsody": 7.35,
    "Green Book": 8.15,
    "The Favourite": 8.75
}

luxury_prices = {
    "A Star Is Born": 10.5,
    "Bohemian Rhapsody": 9.45,
    "Green Book": 10.25,
    "The Favourite": 11.55
}

ultra_luxury_prices = {
    "A Star Is Born": 13.5,
    "Bohemian Rhapsody": 12.75,
    "Green Book": 13.25,
    "The Favourite": 13.95
}

title = input()
room_type = input()
tickets = int(input())
total_income = 0

if room_type == "normal":
    total_income = normal_prices[title] * tickets
elif room_type == "luxury":
    total_income = luxury_prices[title] * tickets
elif room_type == "ultra luxury":
    total_income = ultra_luxury_prices[title] * tickets

print(f"{title} -> {total_income:.2f} lv.")
