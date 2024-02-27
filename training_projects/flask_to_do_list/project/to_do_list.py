from typing import List
from project.section import Section, Task


class ToDoList:
    def __init__(self):
        self.sections: List[Section] = []


todo = ToDoList()
