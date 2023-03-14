from typing import List


class Animal:
    def __init__(self, species: str):
        self.species = species

    def animal_sound(self):
        pass


class Dog(Animal):

    def animal_sound(self):
        return 'woof-woof'


class Cat(Animal):

    def animal_sound(self):
        return 'meow'


class Chicken(Animal):

    def animal_sound(self):
        return 'tweet'


class Cow(Animal):

    def animal_sound(self):
        return 'moo'


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.animal_sound())


animals = [Cat('cat'), Dog('dog'), Chicken('chicken')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
#
