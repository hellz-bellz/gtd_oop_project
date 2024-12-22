import unittest
from gtd.kanban import KanbanBoard
from gtd.gtd_system import GTDSystem
from gtd.task import Task

class TestKanbanBoard(unittest.TestCase):
    def setUp(self):
        self.gtd_system = GTDSystem(":memory:")
        self.kanban_board = KanbanBoard(self.gtd_system)

    def test_display(self):
        task1 = Task("Test Task 1", status="Ожидает")
        task2 = Task("Test Task 2", status="В процессе")
        self.gtd_system.add_to_inbox(task1)
        self.gtd_system.add_to_inbox(task2)

        try:
            self.kanban_board.display()
        except Exception as e:
            self.fail(f"KanbanBoard.display() вызвал ошибку: {e}")

if __name__ == "__main__":
    unittest.main()
