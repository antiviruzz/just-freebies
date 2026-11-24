import random

score = 0
question = [
    {
        "question1": "What is the capital of Nigeria?",
        "options": ["Kwara", "Kano", "Abuja", "Imo"],
        "answer": "Abuja"
    },
    {
        "question1": "What is my name?",
        "options": ["Rid", "Tao", "Yuu", "Rii"],
        "answer": "Rid"
    },
    {
        "question1": "What color is this?",
        "options": ["Red", "Blue", "Green", "Pink"],
        "answer": "Pink"
    }
]

random.shuffle(question)

for que in question:
    print(que["question1"])
    letters = ["A", "B", "C", "D"]
    for i, opt in enumerate(que["options"]):
        print(f"{letters[i]}. {opt}")

    while True:
        choice = input("Select an answer: ").strip().capitalize()
        if choice not in(letters):
            print("Select a valid option")
            continue
        break
    index = letters.index(choice)
    sel_ans = que["options"][index]
    print(f"You selected: {sel_ans}")
    if sel_ans == que["answer"]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
print(f"Score: {score}")
percentage = score/len(question) * 100
print(f"Percentage: {percentage:.2f}%")