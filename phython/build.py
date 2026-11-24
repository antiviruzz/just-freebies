print("welcome to Unique Ridwan POS Terminal!")
password = 1997
balance = 10000

name = input("What is your full name? ")
age = input("How old are you? ")
pin = int(input("Enter Pin: "))
if pin != password:
	print("Incorrect Password!")
else:
	amount = int(input("How much do you wish to withdraw? "))

	if amount<= balance:
		balance = balance - amount
		print(f"Remaining balance: {balance}.")
		print(f"{amount} has been successfully withdrawn")
		print("Transaction Successfull")
	else:
		print("Insufficient Balance!")
		print("You cannot withdraw above 10,000")
