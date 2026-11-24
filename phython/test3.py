import json


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expenses saved successfully.")


def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category: ").strip()

        if category == "":
            print("Category cannot be empty.")
            return

        description = input("Enter description: ").strip()

        if description == "":
            print("Description cannot be empty.")
            return

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)

        print("Expense added successfully.")

    except ValueError:
        print("Please enter a valid number for the amount.")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\n===== ALL EXPENSES =====")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. ₦{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']}"
        )


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    return total


def show_total(expenses):
    total = calculate_total(expenses)

    print(f"Total spending: ₦{total:.2f}")


def spending_by_category(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    if len(category_totals) == 0:
        print("No expenses recorded.")
        return

    print("\n===== SPENDING BY CATEGORY =====")

    for category, total in category_totals.items():
        print(f"{category}: ₦{total:.2f}")


def delete_expense(expenses):
    if len(expenses) == 0:
        print("No expenses to delete.")
        return

    view_expenses(expenses)

    try:
        number = int(input("Enter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        deleted_expense = expenses.pop(number - 1)

        print(
            f"Deleted: ₦{deleted_expense['amount']:.2f} | "
            f"{deleted_expense['category']} | "
            f"{deleted_expense['description']}"
        )

    except ValueError:
        print("Please enter a valid number.")


def display_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Calculate total spending")
    print("4. Spending by category")
    print("5. Delete expense")
    print("6. Save expenses")
    print("7. Exit")


def main():
    expenses = load_expenses()

    while True:
        display_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            spending_by_category(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            save_expenses(expenses)

        elif choice == "7":
            save_expenses(expenses)
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-7.")


main()