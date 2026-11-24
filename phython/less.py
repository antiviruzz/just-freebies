import json

expenses = []

def add_expense():
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ").capitalize()
    description = input("Enter the description: ").capitalize()

    expense = {
        "Amount" : amount,
        "Category": category,
        "Description": description
    }
    expenses.append(expense)


def view_expenses():
    if not expenses:
        print("No record in expeses.")
        return
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. #{expense["Amount"]} | {expense["Category"]} | {expense["Description"]}")


def total_spending():
    Total = sum(expense["Amount"] for expense in expenses)
    print(f"The total spending: #{Total}")


def category_spending():
    category_total = {}
    for expense in expenses:
        if expense["Category"] in category_total:
            category_total[expense["Category"]] += expense["Amount"]
        else:
            category_total[expense["Category"]] = expense["Amount"]
    print(category_total)


def delete_expense():
    try:
        to_del = int(input("Which expense no. would you like to delete? "))
        if to_del >= 1 and to_del <= len(expenses):
            del expenses[to_del - 1]
            view_expenses()
            total_spending()
            category_spending()
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please, choose a number!")

    print()


def save_expenses():
    with open("Expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


print("===== EXPENSE_TRACKER =====")
print("Welcome to Unique-Tracker!")


choice = int(input("How many expense would you like to Track? "))

for i in range(choice):
    add_expense()

view_expenses()
total_spending()
category_spending()
delete_expense()
save_expenses()