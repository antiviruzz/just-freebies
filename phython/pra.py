import random

print("Welcome to Dice Rolling!")

player_1 = input("What is your name?").capitalize()
player_2 = input("What is your name?").capitalize()

player1_choice = random.randint(1,6)
print(f"{player_1} rolled {player1_choice}")
player2_choice = random.randint(1,6)
print(f"{player_2} rolled {player2_choice}")

if player1_choice > player2_choice:
    print(f"{player_1} won!")
elif player1_choice == player2_choice:
    print("It's a draw! Roll again.")
else:
    print(f"{player_2} won!")