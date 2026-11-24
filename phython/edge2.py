import json

expenses = []

def add_expenses():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("Amount cannot be less than or equal to zero!")
                continue
            break
        except ValueError:
            print("Kindly enter amount in numbers.")

    while True:
        category = input("Specify the category: ").strip().capitalize()
        if not category:
            print("category cannot be empty.")
            continue
        if not any(char.isalpha() for char in category):
            print("Specify the category with letter(s)")
            continue
        break

    while True:
        description = input("Give a description: ").strip().capitalize()
        if not description:
            print("description cannot be empty.")
            continue
        if not any(char.isalpha() for char in description):
            print("write a  meaningful description.")
            continue
        break

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)

def view_expenses():
    if not expenses:
        print("No record in expenses!")
        return
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ₦{expense["amount"]:,.2f} | {expense["category"]} | {expense["description"]}")

def total_spending():
    total = sum(expense["amount"] for expense in expenses)
    print(f"The total spending: #{total}")

def category_spending():
    if not expenses:
        print("No record in expenses.")
        return
    category_total = {}
    for expense in expenses:
        if expense["category"] in category_total:
            category_total[expense["category"]] += expense["amount"]
        else:
            category_total[expense["category"]] = expense["amount"]
    print(category_total)

def delete_expense():
    try:
        to_del = int(input("Which expense no. would you like to delete? "))
        if to_del >= 1 and to_del <= len(expenses):
            del expenses[to_del - 1]
            print("Expense deleted successfully.")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please, choose a number!")

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

print("===== EXPENSE- TRACKER =====")
print("          MENU LIST         ")

expenses = load_expenses()

while True:
    print("""
    1. Add expense(s)
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
        add_expenses()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        total_spending()
    elif choice == 4:
        category_spending()
    elif choice == 5:
        delete_expense()
    elif choice == 6:
        save_expenses()
    elif choice == 7:
        save_expenses()
        print("Goodbye! Thank you for coming.")
        break
    else:
        print("Invalid choice.")