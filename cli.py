import typer
from gtd.gtd_system import GTDSystem
from gtd.task import Task

app = typer.Typer()

# Инициализируем систему GTD
gtd_system = GTDSystem()


@app.command()
def add_task(title: str, due_date: str = typer.Option(None), priority: int = 0, tags: str = ""):
    """Добавить задачу в Inbox."""
    tag_list = tags.split(",") if tags else []
    task = Task(title, due_date=due_date, priority=priority, tags=tag_list)
    gtd_system.add_to_inbox(task)
    typer.echo(f"Задача '{title}' добавлена в Inbox.")


@app.command()
def list_tasks():
    """Показать задачи в Inbox."""
    if not gtd_system.inbox:
        typer.echo("Inbox пуст.")
    else:
        typer.echo("Задачи в Inbox:")
        for task in gtd_system.inbox:
            typer.echo(f"  - {task}")


@app.command()
def create_project(name: str, tags: str = ""):
    """Создать новый проект."""
    tag_list = tags.split(",") if tags else []
    gtd_system.create_project(name, tags=tag_list)
    typer.echo(f"Проект '{name}' создан.")


@app.command()
def add_task_to_project(task_title: str, project_name: str):
    """Добавить задачу в проект."""
    task = next((t for t in gtd_system.inbox if t.title == task_title), None)
    if not task:
        typer.echo(f"Задача '{task_title}' не найдена в Inbox.")
        return
    try:
        gtd_system.move_to_project(task, project_name)
        typer.echo(f"Задача '{task_title}' добавлена в проект '{project_name}'.")
    except ValueError as e:
        typer.echo(f"Ошибка: {e}")


@app.command()
def list_projects():
    """Показать список проектов и их задачи."""
    gtd_system.display_projects()


@app.command()
def schedule(period: str = typer.Option("day", help="Период: day, week, month")):
    """Показать расписание задач."""
    gtd_system.display_schedule(period)


@app.command()
def add_habit(name: str, target_days: int):
    """Добавить привычку."""
    gtd_system.habit_tracker.add_habit(name, target_days)
    typer.echo(f"Привычка '{name}' добавлена с целью выполнения {target_days} дней.")


@app.command()
def mark_habit_done(name: str):
    """Отметить прогресс по привычке."""
    try:
        gtd_system.habit_tracker.mark_done(name)
        typer.echo(f"Прогресс по привычке '{name}' отмечен.")
    except ValueError as e:
        typer.echo(f"Ошибка: {e}")


@app.command()
def list_habits():
    """Показать прогресс по привычкам."""
    progress = gtd_system.habit_tracker.get_progress()
    if not progress:
        typer.echo("Нет добавленных привычек.")
    else:
        typer.echo("Прогресс по привычкам:")
        for habit, status in progress.items():
            typer.echo(f"  - {habit}: {status}")


if __name__ == "__main__":
    app()