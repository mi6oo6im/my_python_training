from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price:

            if self.__animal_capacity > len(self.animals):
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

            return "Not enough space for animal"

        return "Not enough budget"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return"Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        total_salaries = sum([w.salary for w in self.workers])

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_money_for_care = sum([a.money_for_care for a in self.animals])

        if self.__budget >= total_money_for_care:
            self.__budget -= total_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions_list = list(filter(lambda a: a.__class__.__name__ == 'Lion', self.animals))
        tigers_list = list(filter(lambda a: a.__class__.__name__ == 'Tiger', self.animals))
        cheetahs_list = list(filter(lambda a: a.__class__.__name__ == 'Cheetah', self.animals))

        total_animals_count = len(self.animals)
        amount_of_lions = len(lions_list)
        amount_of_tigers = len(tigers_list)
        amount_of_cheetahs = len(cheetahs_list)

        lions = '\n'.join([lion.__repr__() for lion in lions_list])
        tigers = '\n'.join([tiger.__repr__() for tiger in tigers_list])
        cheetahs = '\n'.join([cheetah.__repr__() for cheetah in cheetahs_list])

        return f"You have {total_animals_count} animals\n"\
               f"----- {amount_of_lions} Lions:\n" + lions + '\n'\
               f"----- {amount_of_tigers} Tigers:\n" + tigers + '\n'\
               f"----- {amount_of_cheetahs} Cheetahs:\n" + cheetahs

    def workers_status(self) -> str:
        keepers_list = list(filter(lambda w: w.__class__.__name__ == 'Keeper', self.workers))
        caretakers_list = list(filter(lambda w: w.__class__.__name__ == 'Caretaker', self.workers))
        vets_list = list(filter(lambda w: w.__class__.__name__ == 'Vet', self.workers))

        total_workers_count = len(self.workers)
        amount_of_keepers = len(keepers_list)
        amount_of_caretakers = len(caretakers_list)
        amount_of_vets = len(vets_list)

        keepers = '\n'.join([keeper.__repr__() for keeper in keepers_list])
        caretakers = '\n'.join([caretaker.__repr__() for caretaker in caretakers_list])
        vets = '\n'.join([vet.__repr__() for vet in vets_list])

        return f"You have {total_workers_count} workers\n"\
               f"----- {amount_of_keepers} Keepers:\n" + keepers + '\n'\
               f"----- {amount_of_caretakers} Caretakers:\n" + caretakers + '\n'\
               f"----- {amount_of_vets} Vets:\n" + vets
