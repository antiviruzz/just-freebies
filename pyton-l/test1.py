expenses = []

expense1 = {
    "amount": 5000,
    "category": "Food",
    "description": "Bought rice" 
}
expenses.append(expense1)

expense2 = {
    "amount": 3000,
    "category": "Transport",
    "description": "Uber ride"
}
expenses.append(expense2)

expense3 = {
    "amount": 2000,
    "category": "Data",
    "description": "Internet subscription"
}
expenses.append(expense3)

expense4 = {
    "amount": 1500,
    "category": "Food",
    "description": "Bought bread"
}
expenses.append(expense4)

for i, expense in enumerate(expenses, start=1):
    print(f"{i}. ₦{expense["amount"]} | {expense["category"]} | {expense["description"]}")

total = sum(expense["amount"] for expense in expenses)
print(f"Total spending: {total}")

category_spending = {}
for expense in expenses:
    if expense["category"] in category_spending:
        category_spending[expense["category"]] += expense["amount"]
    else:
        category_spending[expense["category"]] = expense["amount"]
for i, (category, amount) in enumerate (category_spending.items(), start=1):
    print(f"{i}. {category} || {amount}")
