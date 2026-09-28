tasks = []
while True:
    print("\nСписок задач")
    print("1. Добавить задачу")
    print("2. Показать задачу")
    print("3. Удалить задачу")
    print("4. Выйти")

    choice = input("Выберите действие:")

    if choice == "1":
        task = input("Введите задачу:")
        tasks.append(task)
        print("Задача добавлена.")

    elif choice == "2":
        if len(tasks) == 0:
            print("Список задач.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}.{tasks[i]}")
    elif choice == "3":
        if len(tasks) == 0:
            print("Список задач пуст.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}.{tasks[i]}")
                number = int(input("Введите номер задачи для удаления: "))
                if number >= 1 and number >=1 and number <= len(tasks):
                    tasks.pop(number - 1)
                    print("Задача удалена.")
                else:
                    print("Такой задачи нет.")
    elif choice == "4":
        print("Программа завершена.")
        break
    else:
        print("Неверный пункт меню.")
                