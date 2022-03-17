# Roses, Dahlias, Tulips, Narcissus, Gladiolus

# Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# Ако Нели купи повече от 90 Далии - 15% отстъпка от крайната цена;
# Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.

flower = input()
num_flower = int(input())
budget = int(input())
difference = 0

flower_cost = {
    "Roses": 5.0,
    "Dahlias": 3.8,
    "Tulips": 2.8,
    "Narcissus": 3.0,
    "Gladiolus": 2.5
}

cost = num_flower * flower_cost[flower]

if flower == "Roses" and num_flower > 80:
    cost *= 0.9
elif flower == "Dahlias" and num_flower > 90:
    cost *= 0.85
elif flower == "Tulips" and num_flower > 80:
    cost *= 0.85
elif flower == "Narcissus" and num_flower < 120:
    cost *= 1.15
elif flower == "Gladiolus" and num_flower < 80:
    cost *= 1.20

difference = abs(budget - cost)
# output

if budget >= cost:
    print(f"Hey, you have a great garden with {num_flower} {flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
