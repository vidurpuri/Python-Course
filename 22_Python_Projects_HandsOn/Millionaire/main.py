questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
        "answer": "A"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
        "answer": "B"
    }
]

prizes = [100, 200, 300]
i = 0

for question in questions:
    print(question["question"])
    for option in question["options"]:
        print(option)
    user_answer = input("Your answer (A, B, C, D): ")
    if user_answer.upper() == question["answer"]:
        print("Correct!")
        print("You have won:", prizes[i])
    else:
        print("Wrong answer.")
    i += 1
