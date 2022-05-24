food_in_kg = int(input())
food_in_grams = food_in_kg * 1000
food_is_over = False
inputting = input()
food_eaten = 0

while inputting != "Adopted":
    food_eaten += int(inputting)
    if food_eaten > food_in_grams:
        food_is_over = True
    inputting = input()

difference = abs(food_in_grams - food_eaten)
if food_is_over:
    print(f"Food is not enough. You need {difference} grams more.")
else:
    print(f"Food is enough! Leftovers: {difference} grams.")
