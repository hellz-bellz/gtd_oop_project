from gtd.task import Task

class Project:
    def __init__(self, name, tags=None):
        self.name = name
        self.tasks = []
        self.tags = tags or []
        self.status = "Планируется"

    def add_task(self, task):
        if not isinstance(task, Task):
            raise ValueError("Можно добавлять только объекты класса Task.")
        self.tasks.append(task)

    def __str__(self):
        return f"Проект: {self.name} ({len(self.tasks)} задач)"
