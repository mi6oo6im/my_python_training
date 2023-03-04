from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str) -> str:
        for t in self.tasks:
            if t.name == task_name:
                t.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        removed = 0
        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
                removed += 1
        return f"Cleared {removed} tasks."

    def view_section(self) -> str:
        return f"Section {self.name}:\n" + '\n'.join([f'{t.details()}' for t in self.tasks])


