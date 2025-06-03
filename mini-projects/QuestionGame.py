questions = [
    ["What is ChatGPT?", "An AI chatbot", "A game", "A website", "A movie", 0],
    ["Which of these is a programming language?", "HTML", "CSS", "Python", "Google", 2],
    ["What does CPU stand for?", "Central Process Unit", "Central Processing Unit", "Computer Power Unit", "None", 1],
    ["2 + 2 * 2 = ?", "8", "6", "4", "10", 1],
]

score = 0

for q in questions:
    print("\n" + q[0])  # print the question
    for i in range(1, 5):  # options are at index 1 to 4
        print(f"{i - 1}. {q[i]}")

    user_answer = int(input("Enter your answer (index 0-3): "))

    if user_answer == q[5]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer is: {q[q[5] + 1]}")

print(f"\nYour Final Score: {score}/{len(questions)}")
