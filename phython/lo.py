import random

stone = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

razor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to Rock-Paper Challenge!")

comb = [stone, paper, razor]

user_choice = int(
    input("Choose a number from 0 to 2. 0 for Stone, 1 for Paper, 2 for Razor: ")
)

if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number, you lose!")

else:
    print(f"You chose:{comb[user_choice]}")

    computer_choice = random.randint(0, 2)

    print(f"Computer chose:{comb[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!")

    elif user_choice == 0 and computer_choice == 2:
        print("You win!")

    elif user_choice == 2 and computer_choice == 1:
        print("You win!")

    elif user_choice == 1 and computer_choice == 0:
        print("You win!")

    else:
        print("You lose!")