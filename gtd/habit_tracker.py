from gtd.base_item import BaseItem
from typing import List, Optional

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

class HabitTracker:
    def __init__(self):
        self.habits = {}

    def add_habit(self, title: str, target_days: int, tags: Optional[List[str]] = None):
        """Добавляет привычку в трекер."""
        habit = Habit(title, target_days, tags)
        self.habits[title] = habit

    def mark_done(self, title: str):
        """Отмечает выполнение привычки."""
        if title in self.habits:
            self.habits[title].mark_done()
        else:
            raise ValueError(f"Привычка '{title}' не найдена.")

    def get_progress(self):
        """Возвращает прогресс всех привычек."""
        return {
            title: str(habit)
            for title, habit in self.habits.items()
        }
