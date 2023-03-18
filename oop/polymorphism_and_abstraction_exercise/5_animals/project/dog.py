from project.animal import Animal


class Dog(Animal):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    @staticmethod
    def make_sound():
        return 'Woof!'

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age}" \
               f" year old {self.gender} {self.__class__.__name__}"

