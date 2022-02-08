#Rock Papers Scisoors
import random
import os
import time

def start():
    items = ["rock", "papers", "scissors"]
    user_choice = "".lower()
    computer_choice = ""
    user = 0
    computer = 0
    
    for i in range(5):
        user_choice = input("\nEnter your Choice: ").lower()
        computer_choice = random.choice(items)
        print(f"Computer's Choice: {computer_choice}\n")
        if user_choice == computer_choice:
            time.sleep(0.5)
            print("Tied!")
        
        elif user_choice == "papers" and computer_choice == "rock":
            print("You Win!")
            user += 1
        elif user_choice == "scissors" and computer_choice == "papers":
            print("You Win!")
            user += 1
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You Win!")
            user += 1
        else:
            print("Computer Wins!")
            computer += 1
    
    time.sleep(1.5)
    print(f"Your Score: {user}\nComputer's Score: {computer}")
    if user > computer:
        print("\nYou are the Champion!")
    elif computer > user:
        print("\nComputer is the Chapmion!")
    else:
        print("\nMatch Tied!")

os.system("cls")
time.sleep(1.5)
print("                                       ROCK PAPERS SCISSORS")
time.sleep(2.5)
start()