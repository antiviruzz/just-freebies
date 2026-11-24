import json

expenses = []

def add_exp():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Kindly enter a valid amount!")


    while True:
        category = input("Enter the specific category: ").strip().capitalize()
        if not category:
            print("Category cannot be empty!")
            continue
        if not any(char.isalpha() for char in category):
            print("Kindly enter a better category")
            continue

        break

    while True:
        description = input("Enter the description: ").strip().capitalize()
        if not description:
            print("Description must not be empty")
            continue
        if not any(char.isalpha() for char in description):
            print("Kindly enter a better description")
            continue
        break

    expense = {
        "amount" : amount,
        "category" : category,
        "description" : description
    }

    expenses.append(expense)

def itemize():
    for index, expense in enumerate(expenses, start=1):
        print(index, expense)

add_exp()
itemize()