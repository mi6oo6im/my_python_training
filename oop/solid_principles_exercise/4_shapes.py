########################################################################################################################
#                              ___                        __   ____ _                                                  #
#                             / _ \ _ __   ___ _ __      / /  / ___| | ___  ___  ___                                   #
#                            | | | | '_ \ / _ \ '_ \    / /  | |   | |/ _ \/ __|/ _ \                                  #
#                            | |_| | |_) |  __/ | | |  / /   | |___| | (_) \__ \  __/                                  #
#                             \___/| .__/ \___|_| |_| /_/     \____|_|\___/|___/\___|                                  #
#                                  |_|                                                                                 #
#                                                                                                                      #
#                                                                                                                      #
# The old code violates the Open / Close Principle, because in order to extend the functionality by adding additional  #
# shapes you need to make changes to the Calculator class. This is solved by creating an overarching abstract parent   #
# class Shape inherited by the Rectangle and Triangle classes and adding the calculate_area method to them.            #
#                                                                                                                      #
########################################################################################################################

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        ...


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, base_side, height):
        self.base_side = base_side
        self.height = height

    def calculate_area(self):
        return self.base_side * self.height / 2


class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)

