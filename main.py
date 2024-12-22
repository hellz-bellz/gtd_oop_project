from gtd.gtd_system import GTDSystem
from gtd.task import Task

def main():
    system = GTDSystem()

    # # Создаем задачи
    # task1 = Task("Сделать проект", due_date="2024-12-25", priority=3, tags=["Учеба", "Python"])
    # task2 = Task("Пройти 10 000 шагов", due_date="2024-12-22", priority=2, tags=["Здоровье"])
    # system.add_to_inbox(task1)
    # system.add_to_inbox(task2)

    # # Создаем проект и добавляем в него задачу
    # system.create_project("Учебный проект", tags=["Учеба"])
    # system.move_to_project(task1, "Учебный проект")

    # # Выводим расписание
    # print("\nРасписание на сегодня:")
    # system.display_schedule("day")

    # print("\nСписок проектов:")
    # system.display_projects()

    # # Работа с трекером привычек
    # system.habit_tracker.add_habit("Чтение книги", target_days=7)
    # system.habit_tracker.mark_done("Чтение книги")
    # print("\nТрекер привычек:")
    # print(system.habit_tracker)

if __name__ == "__main__":
    main()
