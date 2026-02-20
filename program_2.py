# By Nolan Nelsen
# Written on 2/20/2026
# Math Quiz

# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

import random

def math_equation(answer):
    answer = 0.0

    number1 = random.randint(1, 999)
    number2 = random.randint(1, 999)

    print(f"What is {number1} + {number2}?")
    answer = float(input("Your answer: "))

    actual_answer = number1 + number2

    if answer == actual_answer:
        print("Congratulations, your answer is correct!")
    else:
        print(f"Your answer is incorrect. The answer is {actual_answer}.")

math_equation(0)


# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect a message showing the correct answer should be displayed.
# The program must use a function that accomplishes part of the needed tasks.
