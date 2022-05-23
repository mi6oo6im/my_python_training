name = input()
house = ''
while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(name) < 5:
        house = 'Gryffindor'
    elif len(name) == 5:
        house = 'Slytherin'
    elif len(name) == 6:
        house = 'Ravenclaw'
    elif len(name) > 6:
        house = 'Hufflepuff'
    print(f"{name} goes to {house}.")
    name = input()
else:
    print("Welcome to Hogwarts.")
