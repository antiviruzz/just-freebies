import json

expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Calculate total spending")
    print("4. Spending by category")
    print("5. Delete expense")
    print("6. Save expenses")
    print("7. Exit")

    choice = input("Choose an option: ")

    # ADD EXPENSE
    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)

        print("Expense added successfully.")

    # VIEW EXPENSES
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\n===== ALL EXPENSES =====")

            for index, expense in enumerate(expenses, start=1):
                print(
                    f"{index}. ₦{expense['amount']:.2f} | "
                    f"{expense['category']} | "
                    f"{expense['description']}"
                )

    # TOTAL SPENDING
    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print(f"Total spending: ₦{total:.2f}")

    # SPENDING BY CATEGORY
    elif choice == "4":
        category_totals = {}

        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]

            if category in category_totals:
                category_totals[category] = category_totals[category] + amount
            else:
                category_totals[category] = amount

        if len(category_totals) == 0:
            print("No expenses recorded.")
        else:
            print("\n===== SPENDING BY CATEGORY =====")

            for category, total in category_totals.items():
                print(f"{category}: ₦{total:.2f}")

    # DELETE EXPENSE
    elif choice == "5":
        if len(expenses) == 0:
            print("No expenses to delete.")
        else:
            for index, expense in enumerate(expenses, start=1):
                print(
                    f"{index}. ₦{expense['amount']:.2f} | "
                    f"{expense['category']} | "
                    f"{expense['description']}"
                )

            number = int(input("Enter expense number to delete: "))

            if number >= 1 and number <= len(expenses):
                deleted_expense = expenses.pop(number - 1)
                print(f"{deleted_expense['description']} deleted.")
            else:
                print("Invalid expense number.")

    # SAVE
    elif choice == "6":
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expenses saved successfully.")

    # EXIT
    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-7.")