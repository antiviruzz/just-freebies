"""
Function to define:
1. add expense
2. view expense
3. total spending
4. spending by category
5. delete expense
6. save expense
7. load expense
"""

import json

expenses = []

def add_exp():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount cannot be less that zero.")
                continue
            if not amount:
                print("Amount cannot be empty.")
                continue
            break
        except ValueError:
            print("Kindly enter a valid amount.")

    while True:
        category = input("Enter category: ").strip().capitalize()
        if not category:
            print("Category cannot be empty.")
            continue
        if not any(char.isalpha() for char in category):
            print("Kindly enter a valid category.")
            continue
        break

    while True:
        description = input("Enter the description: ").strip().capitalize()
        if not description:
            print("Descprition cannot be empty.")
            continue
        if not any(char.isalpha() for char in description):
            print("Kindly enter a valid description.")
            continue
        break

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)


def view_exp():
    if not expenses:
        print("No record in expenses")
        return
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ₦{expense["amount"]:,.2f} | {expense["category"]} | {expense["description"]}")


def total_exp():
    if not expenses:
        print("No record in expenses.")
        return
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: ₦{total:,.2f}")

def cat_ex():
    if not expenses:
        print("No record in expenses.")
        return
    cat_sp = {}
    for expense in expenses:
        if expense["category"] in cat_sp:
            cat_sp[expense["category"]] += expense["amount"]
        else:
            cat_sp[expense["category"]] = expense["amount"]
    print(cat_sp)

def del_exp():
    if not expenses:
        print("No record to delete")
        return
    while True:
        try:
            opt_del = int(input("Select which expense no. to delete? "))
            if opt_del <= 0 or opt_del > len(expenses):
                print("Invalid choice")
                continue
            else:
                del expenses[opt_del-1]
                print("Expense successfully deleted.")
            break
        except ValueError:
            print("Select a valid number.")

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
    print("File saved successfully.")

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

print("===== EXPENSE - TRACKER =====")
print("          MENU LIST          ")
print("=============================")

expenses = load_expenses()

while True:
    print("""
    1. Add expense
    2. View expense(s)
    3. Total spending
    4. Spending by category
    5. Delete expense(s)
    6. Save expense(s)
    7. Exit
    """)
    try:
        choice = int(input("Select a number from the list above: "))
    except ValueError:
        print("Please, select a valid number.")
        continue
    if choice == 1:
        add_exp()
    elif choice == 2:
        view_exp()
    elif choice == 3:
        total_exp()
    elif choice == 4:
        cat_ex()
    elif choice == 5:
        del_exp()
    elif choice == 6:
        save_expenses()
    elif choice == 7:
        save_expenses()
        print("Goodbye! Thank you for coming.")
        break
    else:
        print("Invalid choice.")