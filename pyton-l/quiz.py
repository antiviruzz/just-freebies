from datetime import datetime

while True:
    date_chk = input("Enter due date (DD-MM-YYYY): ")

    try:
        if len(date_chk) != 10:
            raise ValueError

        due_date = datetime.strptime(date_chk, "%d-%m-%Y").date()

        print("Date valid!")
        break

    except ValueError:
        print("Invalid date. Use DD-MM-YYYY, e.g. 05-11-2026.")

today = datetime.today().date()
if due_date < today:
    print("Task overdue!")
elif due_date == today:
    print("Today is the deadline.")
else:
    print("Task not overdue.")