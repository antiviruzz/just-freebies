import random

score = 0

questions = [
    {
        "question": "What is the capital of Kwara State?",
        "option": ["Yola", "Kano", "Ilorin", "Uyo"],
        "ans": "Ilorin"
    },
    {
        "question": "What is my fav color?",
        "option": ["Red", "Yellow", "Blue", "Purple"],
        "ans": "Purple"
    },
    {
        "question": "What is my name?",
        "option": ["Rid", "Olu", "Ola", "Ade"],
        "ans": "Rid"
    }
]

random.shuffle(questions)

for i, que in enumerate(questions, start=1):
    print(f"{i}. {que["question"]}\n")
    letters = ["A", "B", "C", "D"]
    random.shuffle(que["option"])
    for i, opt in enumerate(que["option"]):
        print(f"{letters[i]}. {opt}")
    while True:
        choice = input("Pick an answer: ").strip().capitalize()
        if choice not in letters:
            print("Invalid option")
            print("Kindly select from the options above.")
            continue
        break
    ind = letters.index(choice)
    answer = que["option"][ind]
    print(f"Your selected: {answer}.\n")

    if answer == que["ans"]:
        score += 1
        print("Correct answer!")
    else:
        print("Wrong answer.")
percentage = score/len(questions)*100
print(f"Score: {score}.\nPercentage: {percentage:.2f}%.")
if percentage >= 50.00:
    print("Congratulations! You passed.")
else:
    print("We regret to inform you, you failed.")