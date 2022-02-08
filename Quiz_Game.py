# Quiz Game
import os
import time

def ask_questions(question_dict, answer_dict):
    question = 1
    score = 0
    answer = "".lower()
    
    while question <= 2:
        answer = input(f"{question_dict.get(question)}\n\nAnswer:")
        if answer_dict.get(question) == answer:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")
        question += 1
        time.sleep(1)

    time.sleep(2)
    print(f"\nScore: {score}/10 are correct")


questions = {
    1 : "What is the smallest country in the world?\na) India\nb) Nepal\nc) Vatican City",
    2 : "What is the capital of India?\na) Bangalore\nb) New Delhi\nc)Chennai"
}

answers = {
    1 : "c",
    2 : "b"
}


os.system('cls')
time.sleep(1)
print("\n                                       QUIZ GAME")
time.sleep(2)
print("Instructions:-")
time.sleep(1)
print("a) There are 10 questions")
time.sleep(0.5)
print("b) Each correct answer carries 1 point")
time.sleep(0.5)
print("c) There is no negative marking")
time.sleep(0.5)
print("d) Enter the option number as answer")
print("\nLet's Start!\n")
time.sleep(1)
ask_questions(questions, answers)
print("\nThanks for Playing!")
