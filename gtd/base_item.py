from typing import List, Optional

class BaseItem:
    def __init__(self, title: str, tags: Optional[List[str]] = None):
        self.title = title
        self.tags = tags or []
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Завершено" if self.completed else "Не завершено"
        return f"{self.title} (Статус: {status}, Теги: {', '.join(self.tags)})"
