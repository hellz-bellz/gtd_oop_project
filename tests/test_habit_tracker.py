import unittest
from gtd.habit_tracker import HabitTracker

class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        self.habit_tracker = HabitTracker()

    def test_add_habit(self):
        self.habit_tracker.add_habit("Read Books", target_days=30)
        self.assertIn("Read Books", self.habit_tracker.habits)

    def test_mark_habit_done(self):
        self.habit_tracker.add_habit("Read Books", target_days=30)
        self.habit_tracker.mark_done("Read Books")
        self.assertEqual(self.habit_tracker.habits["Read Books"]["progress"], 1)

    def test_get_progress(self):
        self.habit_tracker.add_habit("Read Books", target_days=30)
        self.habit_tracker.mark_done("Read Books")
        progress = self.habit_tracker.get_progress()
        self.assertEqual(progress["Read Books"], "1 / 30")

if __name__ == "__main__":
    unittest.main()
