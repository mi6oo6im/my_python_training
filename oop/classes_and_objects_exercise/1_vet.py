class Vet:
    animals = []
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name: str) -> str:
        if len(Vet.animals) < self.space:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name in Vet.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self) -> str:
        vet_name = self.name
        number_animals = len(self.animals)
        space_left_in_clinic = self.space - len(Vet.animals)
        return f"{vet_name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
for i in range(6):
    peter.register_animal(str(i))
    res = peter.register_animal("Doggy")
print(peter.info())
print(george.info())
