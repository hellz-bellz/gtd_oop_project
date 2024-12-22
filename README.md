# GTD Task Management System

## Description
This is a task management system inspired by the Getting Things Done (GTD) methodology. It supports task management, project organization, habit tracking, and Kanban visualization.

## Features
- Add and manage tasks.
- Organize tasks into projects.
- View schedules for the day, week, or month.
- Track habits with progress visualization.
- Visualize tasks in a Kanban board.

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
