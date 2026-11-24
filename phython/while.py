import json

expenses = [
    {"category": "Food", "amount": 5000},
    {"category": "Transport", "amount": 3000},
    {"category": "Food", "amount": 2000},
    {"category": "Data", "amount": 4000},
    {"category": "Transport", "amount": 1000}
]
def	check():
	for index, expense in enumerate(expenses, start=1):
		print(index, expense)

check()

cart = {}

for expense in expenses:
    if expense["category"] in cart:
        cart[expense["category"]] += expense["amount"]
    else:
        cart[expense["category"]] = expense["amount"]
print(cart)

choice = int(input("Which expense to del?"))
if choice > 0 and choice <= len(expenses):
	del expenses[choice-1]
else:
      print("Invalid choice!")
check()

with open("test.json", "w") as file:
      json.dump(expenses, file, indent=4)