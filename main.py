tasks = []

while True:
    print("\nСписок задач")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Удалить задачу")
    print("4. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        task = input("Введите задачу: ")

        if task.strip():
            tasks.append(task)
            print("Задача добавлена.")
        else:
            print("Задача не может быть пустой.")

    elif choice == "2":
        if not tasks:
            print("Список задач пуст.")
        else:
            print("\nВаши задачи:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("Список задач пуст.")
        else:
            print("\nВаши задачи:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                number = int(input("Введите номер задачи для удаления: "))

                if 1 <= number <= len(tasks):
                    deleted_task = tasks.pop(number - 1)
                    print(f"Задача «{deleted_task}» удалена.")
                else:
                    print("Такой задачи нет.")

            except ValueError:
                print("Введите именно номер задачи.")

    elif choice == "4":
        print("Программа завершена.")
        break

    else:
        print("Неверный пункт меню. Выберите число от 1 до 4.")