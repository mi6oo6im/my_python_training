########################################################################################################################
#                                                                                                                      #
#                        ___       _             __                                                                    #
#                       |_ _|_ __ | |_ ___ _ __ / _| __ _  ___ ___                                                     #
#                        | || '_ \| __/ _ \ '__| |_ / _` |/ __/ _ \                                                    #
#                        | || | | | ||  __/ |  |  _| (_| | (_|  __/                                                    #
#                       |___|_| |_|\__\___|_|  |_|  \__,_|\___\___|                                                    #
#                                                                                                                      #
#                        ____                                  _   _                                                   #
#                       / ___|  ___  __ _ _ __ ___  __ _  __ _| |_(_) ___  _ __                                        #
#                       \___ \ / _ \/ _` | '__/ _ \/ _` |/ _` | __| |/ _ \| '_ \                                       #
#                        ___) |  __/ (_| | | |  __/ (_| | (_| | |_| | (_) | | | |                                      #
#                       |____/ \___|\__, |_|  \___|\__, |\__,_|\__|_|\___/|_| |_|                                      #
#                                   |___/          |___/                                                               #
#                                                                                                                      #
# The old code was violating the Interface Segregation Principle as the children classes were forced to inherit more   #
# methods from the parent than they could use. This was fixed by creating additional abstract classes mixins Workable  #
# Eatable containing each of eat() and work() methods also there were created 2 additional parent classes              #
# WorkManager and BreakManager.                                                                                        #
#
########################################################################################################################

from abc import ABC, abstractmethod
import time


class Eatable(ABC):

    @staticmethod
    @abstractmethod
    def eat():
        ...


class Workable(ABC):

    @staticmethod
    @abstractmethod
    def work():
        ...


class Worker(Eatable, Workable):

    @staticmethod
    def work():
        print("I'm normal worker. I'm working.")

    @staticmethod
    def eat():
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Eatable, Workable):

    @staticmethod
    def work():
        print("I'm super worker. I work very hard!")

    @staticmethod
    def eat():
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Workable):

    @staticmethod
    def work():
        print("I'm a robot. I'm working....")


class Manager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        ...


class WorkManager(Manager):

    def set_worker(self, worker):
        assert isinstance(worker, Workable), f"`worker` must be of type {Workable.__name__}"

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(Manager):

    def set_worker(self, worker):
        assert isinstance(worker, Eatable), f"`worker` must be of type {Workable.__name__}"

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass
