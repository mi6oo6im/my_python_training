########################################################################################################################
#                                                                                                                      #
#                                ____                            _                                                     #
#                               |  _ \  ___ _ __   ___ _ __   __| | ___ _ __   ___ _   _                               #
#                               | | | |/ _ \ '_ \ / _ \ '_ \ / _` |/ _ \ '_ \ / __| | | |                              #
#                               | |_| |  __/ |_) |  __/ | | | (_| |  __/ | | | (__| |_| |                              #
#                               |____/ \___| .__/ \___|_| |_|\__,_|\___|_| |_|\___|\__, |                              #
#                                          |_|                                     |___/                               #
#                                _                         _                                                           #
#                               (_)_ ____   _____ _ __ ___(_) ___  _ __                                                #
#                               | | '_ \ \ / / _ \ '__/ __| |/ _ \| '_ \                                               #
#                               | | | | \ V /  __/ |  \__ \ | (_) | | | |                                              #
#                               |_|_| |_|\_/ \___|_|  |___/_|\___/|_| |_|                                              #
#                                                                                                                      #
#                                                                                                                      #
# The old code was violating the Dependency Inversion Principle, as the Parent class Worker was dependent on the state #
# of the children classes. This was fixed by creating an abstract class ABSWorker and inherit it in the Worker and     #
# SuperWorker classes.                                                                                                 #
#                                                                                                                      #
########################################################################################################################

from abc import ABC, abstractmethod


class ABCWorker(ABC):
    @abstractmethod
    def work(self):
        ...


class Worker(ABCWorker):

    def work(self):
        print("I'm working!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, ABCWorker), '`worker` must be of type {}'.format(Worker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class SuperWorker(ABCWorker):

    def work(self):
        print("I work very hard!!!")


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
