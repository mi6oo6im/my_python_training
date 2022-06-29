class Zoo:
    __animals = 0

    def __init__(self, zoo_name_1):
        self.zoo_name = zoo_name_1
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        Zoo.__animals += 1
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

    def get_info(self, species):
        current_species = ''
        animals = ''
        if species == 'mammal':
            current_species = 'Mammals'
            animals = ', '.join(self.mammals)
        elif species == 'fish':
            current_species = 'Fishes'
            animals = ', '.join(self.fishes)
        elif species == 'bird':
            current_species = 'Birds'
            animals = ', '.join(self.birds)
        return f"""{current_species} in {self.zoo_name}: {animals}
Total animals: {Zoo.__animals}"""


zoo_name = input()
animal_count = int(input())
zoo = Zoo(zoo_name)
for _ in range(animal_count):
    command_line = input()
    species_1, name_1 = command_line.split()
    zoo.add_animal(species_1, name_1)
print_species = input()
print(zoo.get_info(print_species))
