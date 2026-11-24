print("===== Expense Tracker =====")
while True:
    print("1. Add expense")
    print("2. View expenses")
    print("3. Total spending")
    print("4. Spending by category")
    print("5. Delete expense")
    print("6. Save expenses")
    print("7. Exit")

    choice = input("Choose an option: ")
    if choice == 1:
        print("Adding expense...")
    elif choice == 2:
        print("Viewing expenses...")
    elif choice == 3:
        print("Calculating total spending...")
    elif choice == 4:
        print("Spending by category...")
    elif choice == 5:
        print("Deleting expense...")
    elif choice == 6:
        print("Saving expenses...")
    else:
        print("Option not on the list!")


expenses = []

amount, category, description = input("Enter amount: , Enter category: , Enetr description: ").split(",")
amount = float(amount.strip())
category = category.strip()
description = description.strip()

expense = {
    "amount" : amount,
    "category" : category,
    "description" : description
}

expenses.append(expense)
