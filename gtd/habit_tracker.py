from gtd.base_item import BaseItem
from typing import Optional

class Habit(BaseItem):
    def __init__(self, title: str, target_days: int, tags: Optional[List[str]] = None):
        super().__init__(title, tags)
        self.target_days = target_days
        self.progress = 0

    def mark_done(self):
        self.progress += 1

    def is_completed(self):
        return self.progress >= self.target_days

    def __str__(self):
        status = "Завершено" if self.is_completed() else f"{self.progress} / {self.target_days}"
        return f"{super().__str__()}, Прогресс: {status}"
