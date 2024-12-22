from tinydb import TinyDB, Query
from gtd.task import Task
from gtd.project import Project
from gtd.habit_tracker import HabitTracker
from datetime import datetime, timedelta

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
            }, (query.type == "project") & (query.name == project_name))

        # Сохраняем привычки
        for habit in self.habit_tracker.habits.values():
            self.db.upsert({
                "type": "habit",
                "name": habit.title,
                "target_days": habit.target_days,
                "progress": habit.progress,
                "tags": habit.tags
            }, (query.type == "habit") & (query.name == habit.title))


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
                habit = Habit(
                    title=item["name"],
                    target_days=item["target_days"],
                    tags=item.get("tags", [])
                )
                habit.progress = item["progress"]
                self.habit_tracker.habits[item["name"]] = habit

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
    
    def display_projects(self):
        """Отображает список проектов и их задачи."""
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
    

    def get_tasks_for_period(self, start_date, end_date):
        """Возвращает задачи, которые запланированы на заданный период."""
        tasks = []
        for task in self.inbox:
            if task.due_date and start_date <= datetime.strptime(task.due_date, "%Y-%m-%d") <= end_date:
                tasks.append(task)
        for project in self.projects.values():
            for task in project.tasks:
                if task.due_date and start_date <= datetime.strptime(task.due_date, "%Y-%m-%d") <= end_date:
                    tasks.append(task)
        return tasks

    def display_schedule(self, period="day"):
        """Отображает расписание задач на текущий день, неделю или месяц."""
        now = datetime.now()
        if period == "day":
            start_date = now
            end_date = now + timedelta(days=1)
        elif period == "week":
            start_date = now
            end_date = now + timedelta(days=7)
        elif period == "month":
            start_date = now
            end_date = now + timedelta(days=30)
        else:
            raise ValueError("Допустимые значения для периода: 'day', 'week', 'month'.")

        tasks = self.get_tasks_for_period(start_date, end_date)
        if not tasks:
            print(f"Нет задач на {period}.")
        else:
            print(f"Задачи на {period}:")
            for task in tasks:
                print(f"  - {task}")

    def add_habit(self, name, target_days):
        """Добавить привычку в трекер."""
        self.habit_tracker.add_habit(name, target_days)
        self.save_data() 

    def mark_habit_done(self, name):
        """Отметить выполнение привычки."""
        self.habit_tracker.mark_done(name)  
        self.save_data()
