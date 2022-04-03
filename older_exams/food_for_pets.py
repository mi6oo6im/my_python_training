days = int(input())
total_pet_food = float(input())
biscuits = 0
total_dog_ate = 0
total_cat_ate = 0
percent_food_eaten = 0
dog_ate_percent = 0
cat_ate_percent = 0

for d in range(1, days + 1):
    dog_ate = int(input())
    cat_ate = int(input())
    total_dog_ate += dog_ate
    total_cat_ate += cat_ate
    if d % 3 == 0:
        biscuits += (dog_ate + cat_ate) * 0.1

total_food_eaten = total_dog_ate + total_dog_ate
biscuits = round(biscuits)
percent_food_eaten = (total_dog_ate + total_cat_ate) / total_pet_food * 100
dog_ate_percent = total_dog_ate / (total_dog_ate + total_cat_ate) * 100
cat_ate_percent = total_cat_ate / (total_dog_ate + total_cat_ate) * 100

print(f"Total eaten biscuits: {biscuits}gr.")
print(f"{percent_food_eaten:.2f}% of the food has been eaten.")
print(f"{dog_ate_percent:.2f}% eaten from the dog.")
print(f"{cat_ate_percent:.2f}% eaten from the cat.")
