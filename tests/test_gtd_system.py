import unittest
from gtd.gtd_system import GTDSystem
from gtd.task import Task

class TestGTDSystem(unittest.TestCase):
    def setUp(self):
        self.gtd_system = GTDSystem(":memory:")  # Используем временную базу данных для тестов.

    def test_add_task_to_inbox(self):
        task = Task("Test Task")
        self.gtd_system.add_to_inbox(task)
        self.assertEqual(len(self.gtd_system.inbox), 1)
        self.assertEqual(self.gtd_system.inbox[0].title, "Test Task")

    def test_create_project(self):
        self.gtd_system.create_project("Test Project", tags=["Demo"])
        self.assertIn("Test Project", self.gtd_system.projects)

    def test_move_task_to_project(self):
        task = Task("Test Task")
        self.gtd_system.add_to_inbox(task)
        self.gtd_system.create_project("Test Project")
        self.gtd_system.move_to_project(task, "Test Project")
        self.assertEqual(len(self.gtd_system.inbox), 0)
        self.assertEqual(len(self.gtd_system.projects["Test Project"].tasks), 1)

if __name__ == "__main__":
    unittest.main()
