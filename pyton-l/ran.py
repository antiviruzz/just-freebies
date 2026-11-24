import random

score = 0

questions = [
    {
        "question": "What is the capital of Kwara State?",
        "option": ["Yola", "Kano", "Ilorin", "Uyo"],
        "ans": "Ilorin",
        "marks": 10
    },
    {
        "question": "What is my fav color?",
        "option": ["Red", "Yellow", "Blue", "Purple"],
        "ans": "Purple",
        "marks": 30
    },
    {
        "question": "What is my name?",
        "option": ["Rid", "Olu", "Ola", "Ade"],
        "ans": "Rid",
        "marks": 60
    }
]

letters = ["A", "B", "C", "D"]

def display_que(que):

    print(f"{que["question"]}")

    random.shuffle(que["option"])

    for i, opt in enumerate(que["option"]):
        print(f"{letters[i]}. {opt}")

def get_response():
   while True:

    choice = input("Pick an answer: ").strip().capitalize()

    if choice not in letters:

        print("Invalid option")
        print("Kindly select from the options above.")
        continue
    return choice

def check_answer(selected_resp, que):
    if selected_resp == que["ans"]:
       print("Correct.")
       return True
    else:
       print("Wrong.")
       return False

def show_result(score, total_marks):
    percentage = score/total_marks * 100
    print(f"score: {score}/{total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    if percentage>= 50:
       print("Congratulations! You passed.")
    else:
       print("You failed.")

random.shuffle(questions)
total_marks = sum(que["marks"] for que in questions)

for que in questions:
    display_que(que)
    choice = get_response()
    index = letters.index(choice)
    selected_resp = que["option"][index]
    correct = check_answer(selected_resp, que)
    if correct:
       score+= que["marks"]
show_result(score, total_marks)