import json

from datetime import datetime

def load_tasks():
    required_keys = ["title", "completed", "priority", "date"]
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                for task in data:
                    if not isinstance(task, dict):
                        return []
                    if not all(key in task for key in required_keys):
                        return []
                    if not all([
                        isinstance(task["title"], str),
                        isinstance(task["completed"], bool),
                        isinstance(task["priority"], str),
                        isinstance(task["date"], str)     
                    ]):
                        return []
                return data
            return []
    except FileNotFoundError:
        print("File not found...returning an empty list.")
        return []
    except json.JSONDecodeError:
        print("Warning! File corrupted...returning an empty list.")
        return []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

def main():
    while True:
        print("\n===== MY TODO LIST =====\n")
        print("1. Add Task")
        print("2. View Task")
        print("3. Complete Task")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Filter Task")
        print("7. Sort by Priority")
        print("8. Sort by due-date")
        print("9. Exit")

        try:
            select = int(input("Choose an option: "))

            if select < 1 or select > 9:
                print("Invalid option")
                continue
            elif select == 1:
                add_task()
            elif select == 2:
                view_task()
            elif select == 3:
                complete_task()
            elif select == 4:
                edit_task()
            elif select == 5:
                delete_task()
            elif select == 6:
                filter_task()
            elif select == 7:
                sort_priority()
            elif select == 8:
                sort_due_date()
            elif select == 9:
                print("Thank you for using my Todo-list. Goodbye.")
                break
        except ValueError:
            print("Kindly select a number from the options.")

def add_task():
    while True:
        title = input("Enter task title: ").strip().capitalize()
        if not title:
            print("This colunm cannot be empty.")
            continue
        if not any(char.isalpha() for char in title):
            print("Title must contain atleast one letter.")
            continue
        print("Select Priority: ")
        print("High")
        print("Medium")
        print("Low")
        while True:
            priority = input("Choose priority: ").strip().capitalize()
            if priority not in ["High", "Medium", "Low"]:
                print("Kindly select a valid priority.")
                continue
            while True:
                date_chk = input("Enter due date (DD-MM-YYYY): ")
                try:
                    if len(date_chk) != 10:
                        raise ValueError
                    due_date = datetime.strptime(date_chk, "%d-%m-%Y")
                    break    
                except ValueError:
                    print("Invalid date. Use DD-MM-YYYY, e.g. 05-11-2026.")
            break

        task = {
            "title": title,
            "completed": False,
            "priority": priority,
            "date": date_chk
        }
        tasks.append(task)
        save_tasks()
        print("Task added successfully.")
        break
def view_task():
    if not tasks:
        print("No task available.")
        return
    today = datetime.today().date()
    for i, task in enumerate(tasks, 1):
        if not task["completed"]:
            status = "Pending"
        else:
            status = "Completed"
        due_date = datetime.strptime(task["date"], "%d-%m-%Y").date()
        if task["completed"]:
            alert = "Task completed."
        elif due_date < today:
            alert = "Task overdue!"
        else:
            alert = "Task is on."
        print(f"{i}. Title: {task['title']} || Status: {status} || Priority: {task['priority']} || Due-Date: {task['date']} || Alert: {alert}")
def complete_task():
    if not tasks:
        print("No task available.")
        return
    view_task()
    while True:
        try:
            choice = int(input("Which task would you like to mark completed?(press 0 to cancel): "))
            if choice == 0:
                print("Returning to main-menu...")
                return
            if choice < 1 or choice > len(tasks):
                print("Invalid choice")
                continue
            if tasks[choice-1]["completed"]:
                print("This task has already been completed.")
                continue
            else:
                tasks[choice-1]["completed"] = True
                save_tasks()
                print(f"Task {choice}. successfully completed.")
            break
        except ValueError:
            print("Enter a valid option")

def edit_task():
    if not tasks:
        print("No task available.")
        return
    
    view_task()
    
    while True:
        try:
            choice = int(input("Which task would you like to edit? (press 0 to cancel) "))
            if choice == 0:
                print("Returning to main-menu...")
                return
            if choice < 1 or choice > len(tasks):
                print("Invalid choice.")
                continue
            break
        except ValueError:
            print("Select a valid number.")

    while True:
        print("\nWhat would you like to edit?")
        print("1. Task title")
        print("2. Task priority")
        print("3. Task due-date")
        print("4. Cancel")
        try:
            cho = int(input("Choose an option: "))
            if cho < 1 or cho > 4:
                print("Invalid option.")
                continue
            elif cho == 1:
                while True:
                    new_title = input("Enter the new title: ").strip().capitalize()
                    if not new_title:
                        print("This column cannot be empty.")
                        continue
                    if not any(char.isalpha() for char in new_title):
                        print("New title must contain at least one letter.")
                        continue
                    
                    tasks[choice - 1]["title"] = new_title
                    save_tasks()
                    print("Task successfully edited.")
                    return
            elif cho == 2:
                print("Checking...")
                while True:
                    new_priority = input("Enter new priority (High/Medium/Low): ").strip().capitalize()
                    if new_priority not in ["High", "Medium", "Low"]:
                        print("Kindly select a valid priority.")
                        continue

                    tasks[choice - 1]["priority"] = new_priority
                    save_tasks()
                    print("Task priority updated successfully.")
                    return
            elif cho == 3:
                print("Changing due date...")
                while True:
                    new_due_date = input("Enter new date: ")
                    try:
                        if len(new_due_date) != 10:
                            raise ValueError
                        datetime.strptime(new_due_date, "%d-%m-%Y")
                        tasks[choice-1]["date"] = new_due_date
                        save_tasks()
                        print("Task due date updated successfully")
                        return
                    except ValueError:
                        print("Invalid date. Use DD-MM-YYYY, e.g. 05-11-2026.")
            else:
                print("Edit cancelled.")
                return
        except ValueError:
            print("Select a valid option.")
    
def delete_task():
    if not tasks:
        print("No task available")
        return
    view_task()
    while True:
        try:
            choice = int(input("Which task would you like to delete? (press 0 to cancel) "))
    
            if choice == 0:
                print("Returning to main-menu...")
                return
            if choice < 1 or choice > len(tasks):
                print("Invalid choice.")
                continue
            tasks.pop(choice-1)
            save_tasks()
            print("Task deleted successfully")
            break
        except ValueError:
            print("Use a valid option")

def filter_task():
    if not tasks:
        print("No task available.")
        return
    print("\n==== Filter Tasks ====")
    print("1. Pending Tasks")
    print("2. Completed Tasks")
    print("3. Return to main-menu")

    while True:
        try:
            choice = int(input("Choose an option: "))
            if choice <1 or choice > 3:
                print("Invalid option")
                continue
            if choice == 1:
                print("Cheking pending tasks...")
                print("\n==== Pending Task(s) ====")
                found = False
                count = 1
                for task in tasks:
                    if not task["completed"]:
                        print(f"{count}. {task['title']}")
                        count += 1
                        found = True
                if not found:
                    print("No pending task found.")
                return
            elif choice == 2:
                print("Checking completed tasks...")
                print("\n==== Completed Task(s) ====")
                found = False
                count = 1
                for task in tasks:
                    if task["completed"]:
                        print(f"{count}. {task['title']}")
                        count+= 1
                        found = True
                if not found:
                    print("No completed task found.")
                return
            else:
                print("Returning back to main-menu")
                return
        except ValueError:
            print("Kindly select a valid option.")
def sort_priority():
    if not tasks:
        print("No tasks available to sort.")
        return
    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }
    tasks.sort(key=lambda task: priority_order[task["priority"]])
    print("Priority sorted successfully...")
    view_task()

def sort_due_date():
    if not tasks:
        print("No record available")
        return
    tasks.sort(key=lambda task: datetime.strptime(task["date"], "%d-%m-%Y"))
    print("Tasks sorted by due date successfully.")
    view_task()

main()