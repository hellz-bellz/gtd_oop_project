import unittest
from gtd.project import Project
from gtd.task import Task

class TestProject(unittest.TestCase):
    def test_project_creation(self):
        project = Project("Test Project", tags=["Demo"])
        self.assertEqual(project.name, "Test Project")
        self.assertListEqual(project.tags, ["Demo"])
        self.assertEqual(len(project.tasks), 0)

    def test_add_task_to_project(self):
        project = Project("Test Project")
        task = Task("Test Task")
        project.add_task(task)
        self.assertEqual(len(project.tasks), 1)
        self.assertEqual(project.tasks[0].title, "Test Task")

if __name__ == "__main__":
    unittest.main()
