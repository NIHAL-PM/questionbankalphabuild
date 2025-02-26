# A simple question bank program

# Store questions as a list of dictionaries
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A) Delhi", "B) Mumbai", "C) Kolkata", "D) Chennai"],
        "answer": "A",
        "explanation": "Delhi is the capital city of India."
    },
    {
        "question": "Which river is known as the Ganges?",
        "options": ["A) Yamuna", "B) Ganga", "C) Brahmaputra", "D) Godavari"],
        "answer": "B",
        "explanation": "The Ganga, also called the Ganges, is a major river in India."
    }
]

# Keep track of the user's score and question limit
score = 0
questions_asked = 0
max_free_questions = 2  # Simulating a limit (instead of 10 for testing)

# Main loop to ask questions
while questions_asked < max_free_questions:
    # Pick the current question
    current_question = questions[questions_asked]

    # Show the question and options
    print("\nQuestion:", current_question["question"])
    for option in current_question["options"]:
        print(option)

    # Get the user's answer
    user_answer = input("Your answer (A/B/C/D): ").upper()

    # Check if the answer is correct
    if user_answer == current_question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is", current_question["answer"])

    # Show explanation
    print("Explanation:", current_question["explanation"])

    # Update counters
    questions_asked += 1
    print(f"Score: {score}/{questions_asked}")

# End of free tier
print(f"\nYou've used {questions_asked} questions. Your final score is {score}/{max_free_questions}.")
print("Subscribe for unlimited questions!")