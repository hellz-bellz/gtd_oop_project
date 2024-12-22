from rich.console import Console
from rich.table import Table
from gtd.task import Task

class KanbanBoard:
    def __init__(self, gtd_system):
        self.gtd_system = gtd_system

    def display(self):
        console = Console()
        table = Table(title="Канбан-доска")

        for status in Task.STATUSES:
            table.add_column(status, style="bold")

        rows = []
        max_tasks = max(len([t for t in self.gtd_system.inbox if t.status == s]) for s in Task.STATUSES)
        for i in range(max_tasks):
            row = []
            for status in Task.STATUSES:
                tasks = [t.title for t in self.gtd_system.inbox if t.status == status]
                row.append(tasks[i] if i < len(tasks) else "")
            rows.append(row)

        for row in rows:
            table.add_row(*row)

        console.print(table)
