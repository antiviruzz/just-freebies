import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

while True:
    print("\n==== My Todo List ====")
    print("1. Add task")
    print("2. View task")
    print("3. Complete task")
    print("4. Edit task")
    print("5. Delete task")
    print("6. Filter task")
    print("7. Exit")

    try:
        choice = int(input("Choose an option: "))

        if choice < 1 or choice > 7:
            print("Choose a valid option.")
            continue

    except ValueError:
        print("Choose a valid option.")
        continue

    if choice == 1:
        title = input("Enter task: ").strip().capitalize()

        if not title:
            print("Task cannot be empty.")
            continue

        while True:
            priority = input(
                "Choose priority (High/Medium/Low): "
            ).strip().capitalize()

            if priority not in ["High", "Medium", "Low"]:
                print("Choose a valid priority.")
                continue

            break

        task = {
            "title": title,
            "completed": False,
            "priority": priority
        }

        tasks.append(task)
        save_tasks()

        print("Task added successfully.")

    elif choice == 2:
        if not tasks:
            print("No records in tasks.")
            continue

        for i, task in enumerate(tasks, 1):
            if task["completed"]:
                status = "Completed"
            else:
                status = "Pending"

            priority = task.get("priority", "Medium")

            print(
                f"{i}. {task['title']} || {status} "
                f"|| Priority: {priority}"
            )

    elif choice == 3:
        if not tasks:
            print("No tasks available.")
            continue

        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']}")

        while True:
            try:
                complete = int(
                    input("Which task have you completed? ")
                )

                if complete < 1 or complete > len(tasks):
                    print("Invalid task number.")
                    continue

                tasks[complete - 1]["completed"] = True
                save_tasks()

                print("Task marked as completed.")
                break

            except ValueError:
                print("Enter a valid task number.")

    elif choice == 4:
        if not tasks:
            print("No tasks available.")
            continue

        for i, task in enumerate(tasks, 1):
            priority = task.get("priority", "Medium")

            print(
                f"{i}. {task['title']} "
                f"|| Priority: {priority}"
            )

        while True:
            try:
                task_number = int(
                    input("Which task would you like to edit? ")
                )

                if task_number < 1 or task_number > len(tasks):
                    print("Invalid task number.")
                    continue

                task_index = task_number - 1
                break

            except ValueError:
                print("Enter a valid task number.")

        while True:
            print("\nWhat would you like to edit?")
            print("1. Task title")
            print("2. Task priority")
            print("3. Cancel")

            try:
                sl = int(input("Select an option: "))

                if sl < 1 or sl > 3:
                    print("Choose a valid option.")
                    continue

                if sl == 1:
                    while True:
                        new_title = input(
                            "Enter new title: "
                        ).strip().capitalize()

                        if not new_title:
                            print("Title cannot be empty.")
                            continue

                        if not any(
                            char.isalpha() for char in new_title
                        ):
                            print("Title must contain a letter.")
                            continue

                        break

                    tasks[task_index]["title"] = new_title

                    save_tasks()

                    print("Task title updated successfully!")
                    break

                elif sl == 2:
                    while True:
                        new_priority = input(
                            "Enter new priority (High/Medium/Low): "
                        ).strip().capitalize()

                        if new_priority not in [
                            "High", "Medium", "Low"
                        ]:
                            print(
                                "Choose High, Medium, or Low."
                            )
                            continue

                        break

                    tasks[task_index]["priority"] = new_priority

                    save_tasks()

                    print("Task priority updated successfully!")
                    break

                else:
                    print("Editing cancelled.")
                    break

            except ValueError:
                print("Kindly choose a valid option.")

    elif choice == 5:
        if not tasks:
            print("No tasks available.")
            continue

        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']}")

        while True:
            try:
                delete = int(
                    input("Which task would you like to delete? ")
                )

                if delete < 1 or delete > len(tasks):
                    print("Invalid task number.")
                    continue

                tasks.pop(delete - 1)
                save_tasks()

                print("Task deleted successfully.")
                break

            except ValueError:
                print("Enter a valid task number.")

    elif choice == 6:
        if not tasks:
            print("No tasks available.")
            continue

        print("\n===== Filter Tasks =====")
        print("1. View pending tasks")
        print("2. View completed tasks")
        print("3. Return to main menu")

        while True:
            try:
                ch = int(input("Choose an option: "))

                if ch < 1 or ch > 3:
                    print("Choose a valid option.")
                    continue

                elif ch == 1:
                    found = False

                    for i, task in enumerate(tasks, 1):
                        if not task["completed"]:
                            priority = task.get(
                                "priority", "Medium"
                            )

                            print(
                                f"{i}. {task['title']} "
                                f"|| Pending || Priority: {priority}"
                            )

                            found = True

                    if not found:
                        print("No pending tasks.")

                    break

                elif ch == 2:
                    found = False

                    for i, task in enumerate(tasks, 1):
                        if task["completed"]:
                            priority = task.get(
                                "priority", "Medium"
                            )

                            print(
                                f"{i}. {task['title']} "
                                f"|| Completed || Priority: {priority}"
                            )

                            found = True

                    if not found:
                        print("No completed tasks.")

                    break

                else:
                    break

            except ValueError:
                print("Enter a valid digit.")

    elif choice == 7:
        print("Thank you for using My Todo List. Goodbye!")
        break