import unittest
from gtd.task import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Test Task", due_date="2024-12-31", priority=3, tags=["Test", "Demo"])
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.due_date, "2024-12-31")
        self.assertEqual(task.priority, 3)
        self.assertListEqual(task.tags, ["Test", "Demo"])

    def test_task_status_update(self):
        task = Task("Test Task")
        task.update_status("В процессе")
        self.assertEqual(task.status, "В процессе")

    def test_invalid_status_update(self):
        task = Task("Test Task")
        with self.assertRaises(ValueError):
            task.update_status("Invalid Status")

if __name__ == "__main__":
    unittest.main()
