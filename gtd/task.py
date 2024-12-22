from datetime import datetime
from typing import List, Optional
from gtd.base_item import BaseItem

class Task(BaseItem):
    STATUSES = ["Ожидает", "В процессе", "На проверке", "Завершена"]

    def __init__(self, title: str, due_date: Optional[str] = None, priority: int = 0, context: Optional[str] = None, tags: Optional[List[str]] = None):
        super().__init__(title, tags)
        self.due_date = due_date
        self.priority = priority
        self.context = context or "General"
        self.status = "Ожидает"

    def mark_complete(self):
        self.status = "Завершена"
        self.mark_completed()

    def update_status(self, status: str):
        if status in self.STATUSES:
            self.status = status
        else:
            raise ValueError(f"Недопустимый статус: {status}")

    def __str__(self):
        base_str = super().__str__()
        return f"[{self.status}] {base_str} (Due: {self.due_date}, Priority: {self.priority}, Context: {self.context})"
