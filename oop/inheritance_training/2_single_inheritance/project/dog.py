from project.animal import Animal


class Dog(Animal):
    def bark(self):
        return 'barking...'


sharo = Dog()
print(sharo.bark())
print(sharo.eat())