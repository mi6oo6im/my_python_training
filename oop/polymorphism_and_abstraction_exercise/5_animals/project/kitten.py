from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender='Female')

    @staticmethod
    def make_sound():
        return 'Meow'

