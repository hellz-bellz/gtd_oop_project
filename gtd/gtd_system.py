from tinydb import TinyDB, Query
from gtd.task import Task
from gtd.project import Project
from gtd.habit_tracker import HabitTracker

class GTDSystem:
    def __init__(self, db_path="data/tasks.json"):
        self.inbox = []
        self.projects = {}
        self.habit_tracker = HabitTracker()
        self.db = TinyDB(db_path)
        self.load_data()

    def save_data(self):
        """Сохраняет задачи, проекты и привычки в базу данных."""
        query = Query()

        # Сохраняем задачи
        for task in self.inbox:
            self.db.upsert({
                "type": "task",
                "title": task.title,
                "due_date": task.due_date,
                "priority": task.priority,
                "context": task.context,
                "tags": task.tags,
                "status": task.status,
                "completed": task.completed
            }, (query.type == "task") & (query.title == task.title))

        # Сохраняем проекты
        for project_name, project in self.projects.items():
            self.db.upsert({
                "type": "project",
                "name": project.name,
                "tags": project.tags,
                "tasks": [
                    {
                        "title": task.title,
                        "due_date": task.due_date,
                        "priority": task.priority,
                        "context": task.context,
                        "tags": task.tags,
                        "status": task.status,
                        "completed": task.completed
                    }
                    for task in project.tasks
                ]
            }, (query.type == "project") & (query.name == project.name))

        # Сохраняем привычки
        for habit, data in self.habit_tracker.habits.items():
            self.db.upsert({
                "type": "habit",
                "name": habit,
                "target_days": data["target_days"],
                "progress": data["progress"]
            }, (query.type == "habit") & (query.name == habit))

    def load_data(self):
        """Загружает задачи, проекты и привычки из базы данных."""
        for item in self.db.all():
            if item["type"] == "task":
                task = Task(
                    title=item["title"],
                    due_date=item["due_date"],
                    priority=item["priority"],
                    context=item["context"],
                    tags=item["tags"]
                )
                task.status = item["status"]
                task.completed = item["completed"]
                self.inbox.append(task)
            elif item["type"] == "project":
                project = Project(name=item["name"], tags=item["tags"])
                for task_data in item["tasks"]:
                    task = Task(
                        title=task_data["title"],
                        due_date=task_data["due_date"],
                        priority=task_data["priority"],
                        context=task_data["context"],
                        tags=task_data["tags"]
                    )
                    task.status = task_data["status"]
                    task.completed = task_data["completed"]
                    project.add_task(task)
                self.projects[project.name] = project
            elif item["type"] == "habit":
                self.habit_tracker.habits[item["name"]] = {
                    "target_days": item["target_days"],
                    "progress": item["progress"]
                }

    def add_to_inbox(self, task):
        self.inbox.append(task)
        self.save_data()

    def create_project(self, project_name, tags=None):
        self.projects[project_name] = Project(project_name, tags=tags)
        self.save_data()

    def move_to_project(self, task, project_name):
        if project_name not in self.projects:
            raise ValueError(f"Проект '{project_name}' не найден.")
        self.projects[project_name].add_task(task)
        self.inbox.remove(task)
        self.save_data()
