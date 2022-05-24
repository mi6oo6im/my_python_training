total_gr_biscuits = 0
percent_of_food_eaten = 0
total_dog_ate = 0
total_cat_ate = 0
total_eaten = 0
percent_eaten_by_the_dog = 0
percent_eaten_by_the_cat = 0

days = int(input())
initial_food = float(input())

dog_eat = 0
cat_eat = 0
for day in range(1, days + 1):
    dog_eat = int(input())
    cat_eat = int(input())
    both_eat = dog_eat + cat_eat
    total_dog_ate += dog_eat
    total_cat_ate += cat_eat
    total_eaten += both_eat
    if day % 3 == 0:
        total_gr_biscuits += both_eat * 0.1
total_gr_biscuits = round(total_gr_biscuits)
percent_of_food_eaten = total_eaten / initial_food * 100
percent_eaten_by_the_dog = total_dog_ate / total_eaten * 100
percent_eaten_by_the_cat = total_cat_ate / total_eaten * 100

print(f"Total eaten biscuits: {total_gr_biscuits}gr.")
print(f"{percent_of_food_eaten:.2f}% of the food has been eaten.")
print(f"{percent_eaten_by_the_dog:.2f}% eaten from the dog.")
print(f"{percent_eaten_by_the_cat:.2f}% eaten from the cat.")
