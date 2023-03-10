class Robot:
    _sensors_amount = 1

    def __init__(self, name):
        self.name = name

    def sensors_amount(self):
        return self._sensors_amount


class MedicalRobot(Robot):
    _sensors_amount = 6

    def sensors_amount(self):
        return self._sensors_amount


class ChefRobot(Robot):
    _sensors_amount = 4

    def sensors_amount(self):
        return self._sensors_amount


class WarRobot(Robot):
    _sensors_amount = 12

    def sensors_amount(self):
        return self._sensors_amount


def number_of_robot_sensors(robot: Robot):
    print(robot.sensors_amount())


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)
number_of_robot_sensors(griffin)
