# Define the quiz questions and answers
quiz = {
    "What is the capital of France?": {"question": "What is the capital of France?", "answer": "Paris"},
    "What is the capital of Germany?": {"question": "What is the capital of Germany?", "answer": "Berlin"},
    "What is the capital of Italy?": {"question": "What is the capital of Italy?", "answer": "Rome"},
    # Add more questions here
       }

# Initialize the score
score = 0

# Define the check_ans function
def check_ans(question, ans, attempts, score):
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
        return False

# Ask the questions
for question in quiz:
    attempts = 3
    while attempts > 0:
        print(quiz[question]['question'])
        answer = input("Enter Answer: ")
        check = check_ans(question, answer, attempts, score)
        if check:
            score += 1
            break
        attempts -= 1

print(f"Your final score is {score}!")
