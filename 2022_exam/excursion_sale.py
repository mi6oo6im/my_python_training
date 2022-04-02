total_sales = 0
sea_excursions_left = int(input())
mountain_excursions_left = int(input())
command = input()
all_sold = False

while command != "Stop":
    if command == "sea" and sea_excursions_left > 0:
        sea_excursions_left -= 1
        total_sales += 680
    elif command == "mountain" and mountain_excursions_left > 0:
        mountain_excursions_left -= 1
        total_sales += 499
    if mountain_excursions_left == 0 and sea_excursions_left == 0:
        all_sold = True
        break
    command = input()

if all_sold:
    print("Good job! Everything is sold.")

print(f"Profit: {total_sales} leva.")
