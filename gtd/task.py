from datetime import datetime

class Task:
    STATUSES = ["Ожидает", "В процессе", "На проверке", "Завершена"]

    def __init__(self, title, due_date=None, priority=0, context=None, tags=None):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.context = context or "General"
        self.tags = tags or []
        self.status = "Ожидает"
        self.completed = False

    def mark_complete(self):
        self.status = "Завершена"
        self.completed = True

    def update_status(self, status):
        if status in self.STATUSES:
            self.status = status
        else:
            raise ValueError(f"Недопустимый статус: {status}")

    def __str__(self):
        tags_str = ", ".join(self.tags)
        return f"[{self.status}] {self.title} (Due: {self.due_date}, Priority: {self.priority}, Tags: {tags_str})"
