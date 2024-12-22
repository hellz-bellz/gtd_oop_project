class HabitTracker:
    def __init__(self):
        self.habits = {}

    def add_habit(self, name, target_days):
        self.habits[name] = {"target_days": target_days, "progress": 0}

    def mark_done(self, name):
        if name in self.habits:
            self.habits[name]["progress"] += 1
        else:
            raise ValueError(f"Привычка '{name}' не найдена.")

    def get_progress(self):
        return {
            habit: f"{data['progress']} / {data['target_days']}"
            for habit, data in self.habits.items()
        }
