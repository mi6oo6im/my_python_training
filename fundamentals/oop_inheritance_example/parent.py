from inheritance_example_oop.grand_parent import GrandParent


class Parent(GrandParent):
    def __init__(self, name, age):
        GrandParent.__init__(self, name)
        self.age = age

    def get_age(self):
        return self.age
