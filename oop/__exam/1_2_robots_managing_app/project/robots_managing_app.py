from typing import List
from project.robots.base_robot import BaseRobot
from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    @property
    def valid_robot_types(self):
        return {
            "MaleRobot": MaleRobot,
            "FemaleRobot": FemaleRobot,
        }

    @property
    def valid_service_types(self):
        return {
            "MainService": MainService,
            "SecondaryService": SecondaryService,
        }

    def add_service(self, service_type: str, name: str):
        if service_type not in self.valid_service_types:
            raise Exception("Invalid service type!")

        new_service = self.valid_service_types[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.valid_robot_types:
            raise Exception("Invalid robot type!")

        new_robot = self.valid_robot_types[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    @property
    def suitable_service_types(self):
        return {
            "MaleRobot": MainService,
            "FemaleRobot": SecondaryService,
        }

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = next(filter(lambda r: r.name == robot_name, self.robots))
        service = next(filter(lambda s: s.name == service_name, self.services))

        if not isinstance(service, self.suitable_service_types[robot.__class__.__name__]):
            return "Unsuitable service."

        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))

        try:
            robot = next(filter(lambda r: r.name == robot_name, service.robots))
        except StopIteration:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = next(filter(lambda s: s.name == service_name, self.services))

        total_price = sum([r.price for r in service.robots])

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = '\n'.join([s.details() for s in self.services])

        return result
