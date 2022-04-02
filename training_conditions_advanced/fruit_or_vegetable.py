product = input()

is_fruit = product in ("banana", "apple", "kiwi", "cherry", "lemon", "grapes")

is_vegy = product in ("tomato", "cucumber", "pepper", "carrot")

if is_fruit:
    print("fruit")
elif is_vegy:
    print("vegetable")
else:
    print("unknown")
