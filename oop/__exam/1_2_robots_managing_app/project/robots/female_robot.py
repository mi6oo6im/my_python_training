from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, 7)

    @property
    def incremental_kg(self):
        return 1
