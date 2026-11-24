"""
funtions to check:
1. save expenses
2. load expenses
3. add expenses
4. view expenses
5. total expenses
6. category spending
7. delete expenses
"""
import json

expenses = []

def save_expenses():
    with open("expenses.jso", "w") as file:
        json.dump(expenses, file, indent=4)
    print("File has be saved successfully.")

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_expense():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if not amount:
                print("Amount cannot be empty.")
                continue
            if amount <= 0:
                print("Amount cannot be less than or equals to zero.")
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
            print("Category must contain a letter.")
            continue
        break
    while True:
        description = input("Enter the description: ").strip().capitalize()
        if not description:
            print("Description cannot be empty.")
            continue
        if not any(char.isalpha() for char in description):
            print("Description must contain a letter.")
            continue
        break
    expense = {
        "amount": amount,
        "category": category,
        "description": description
	}
    expenses.append(expense)

def view_expense():
    if not expenses:
        print("No record in expenses.")
        return
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. #{expense["amount"]:,.2f} || {expense["category"]} || {expense["description"]}")

def total_expense():
    if not expenses:
        print("No record in expenses.")
        return
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: #{total:,.2f}")

def category_total():
    if not expenses:
        print("No record in expenses.")
        return
    cat_tt = {}
    for expense in expenses:
        if expense["category"] in cat_tt:
            cat_tt[expense["category"]] += expense["amount"]
        else:
            cat_tt[expense["category"]] = expense["amount"]
    print(f"{cat_tt:,.2f}")

