# GTD Task Management System

## Description
This is a task management system inspired by the Getting Things Done (GTD) methodology. It supports task management, project organization, habit tracking, and Kanban visualization.

## Features
- Add and manage tasks.
- Organize tasks into projects.
- View schedules for the day, week, or month.
- Track habits with progress visualization.
- Visualize tasks in a Kanban board.

## Structure
```bash
/gtd_project/
├── gtd/
│   ├── __init__.py
│   ├── task.py
│   ├── project.py
│   ├── gtd_system.py
│   ├── kanban.py
│   ├── habit_tracker.py
│   ├── exceptions.py
├── tests/
│   ├── test_task.py
│   ├── test_project.py
│   ├── test_gtd_system.py
│   ├── test_habit_tracker.py
│   └── test_kanban.py
├── requirements.txt
├── README.md
├── cli.py
└── main.py
```


## Installation
```bash
pip install -r requirements.txt
```

## Usage
Run the CLI:
```bash
python cli.py
```

### Commands
Add a task:
  ```bash
  python cli.py add-task "Task Title" --due-date "2024-12-25" --priority 3 --tags "Tag1,Tag2"
  ```
List all tasks:
  ```bash
  python cli.py list-tasks
  ```
Add a habit:
  ```bash
  python cli.py add-habit "Read a book" --target-days 30
  ```

## Пример работы GTD-системы

![Пример работы GTD-системы](gtd_tasks_DL.png)
