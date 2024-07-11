import random

def multiplication_game():
    score = 0
    for i in range(20):
        num1 = random.randint(1, 11)
        num2 = random.randint(1, 11)
        correct_answer = num1 * num2
        user_answer = int(input(f"What is {num1} x {num2}? "))
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {correct_answer}.")
    print(f"Your final score is {score} out of 20.")

multiplication_game()