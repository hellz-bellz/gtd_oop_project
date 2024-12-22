from gtd.task import Task
from gtd.project import Project
from gtd.habit_tracker import HabitTracker
from gtd.exceptions import TaskNotFoundError

class GTDSystem:
    def __init__(self):
        self.inbox = []
        self.projects = {}
        self.habit_tracker = HabitTracker()

    def add_to_inbox(self, task):
        self.inbox.append(task)

    def create_project(self, project_name, tags=None):
        self.projects[project_name] = Project(project_name, tags)

    def move_to_project(self, task, project_name):
        if project_name not in self.projects:
            raise TaskNotFoundError(f"Проект '{project_name}' не найден.")
        self.projects[project_name].add_task(task)
        self.inbox.remove(task)

    def display_projects(self):
        if not self.projects:
            print("Нет проектов.")
        else:
            print("Список проектов и их задачи:")
            for project_name, project in self.projects.items():
                print(f"\nПроект: {project_name} (Теги: {', '.join(project.tags)})")
                if not project.tasks:
                    print("  Нет задач.")
                else:
                    for task in project.tasks:
                        print(f"  - {task}")
