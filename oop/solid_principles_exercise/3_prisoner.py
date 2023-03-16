########################################################################################################################
#                         _     _     _                                                                                #
#                        | |   (_)___| | _______   __                                                                  #
#                        | |   | / __| |/ / _ \ \ / /                                                                  #
#                        | |___| \__ \   < (_) \ V /                                                                   #
#                        |_____|_|___/_|\_\___/ \_/                                                                    #
#                                                                                                                      #
#                                   _         _   _ _         _   _                                                    #
#                         ___ _   _| |__  ___| |_(_) |_ _   _| |_(_) ___  _ __                                         #
#                        / __| | | | '_ \/ __| __| | __| | | | __| |/ _ \| '_ \                                        #
#                        \__ \ |_| | |_) \__ \ |_| | |_| |_| | |_| | (_) | | | |                                       #
#                        |___/\__,_|_.__/|___/\__|_|\__|\__,_|\__|_|\___/|_| |_|                                       #
#                                                                                                                      #
#                                                                                                                      #
# The old code is violating the Liskov Substitution Principle as the instance of a child class Prisoner can't  fully   #
# replace an instance of the parent class Person. As a solution a second child class FreePerson is created to handle   #
# the walk methods                                                                                                     #
#                                                                                                                      #
########################################################################################################################

import copy


class Person:

    def __init__(self, position):
        self.position = position


class FreePerson(Person):

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super().__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False


prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")

