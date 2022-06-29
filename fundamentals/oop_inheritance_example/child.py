from inheritance_example_oop.parent import Parent


class Child(Parent):
    def __init__(self, name, age, gender):
        Parent.__init__(self, name, age)
        self.gender = gender

    def get_gender(self):
        return self.gender


test = Child("Petar", 35, "M")
print(test.get_name())
print(test.get_age())
print(test.get_gender())