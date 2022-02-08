import time
import random
import os


def user_guess(xs, xe):
	guess = 0
	secret = int(random.randint(xs, xe))
	while guess != secret:
		guess = int(input(f"Guess a number between {xs} and {xe}: "))
		if guess > secret:
			print("Too higher. Guess again.")
		elif guess < secret:
			print("Too lower. Guess again.")
	
	print()
	print(f"Yes, you have guessed the number {secret}, correctly!")


def computer_guess(ys, ye):
	high = ye
	low = ys
	num = 0
	feedback = ""
	time.sleep(1)
	while high == low:
		num = low
	
	while feedback != "C":
		num = random.randint(low, high)
		feedback = input(f"Is {num} the correct number?\n Is it higher(H), or lower(L) or correct(C): ").upper()
		if feedback == "H":
			high = num - 1
		elif feedback == "L":
			low = num + 1
	print()
	print(f"Yay, I have guessed the number {num} correctly!")


os.system('cls')
time.sleep(1)
print()
print("                                       GUESS THE NUMBER GAME")
time.sleep(2)
i = 0
while i < 1:
	print()
	print("Does the user:\n 1. Wants itself to guess a number (Y)? or\n 2. Wants the computer to guess a number(C)?\n\n ")
	time.sleep(3)
	start = input("Reply: ").upper()
	if start == "Y":
		print()
		yrs = int(input("Enter range start: "))
		yre = int(input("Enter range end: "))
		print()
		user_guess(yrs, yre)
	elif start == "C":
		print()
		crs = int(input("Enter range start: "))
		cre = int(input("Enter range end: "))
		print()
		computer_guess(crs, cre)
	print()
	time.sleep(1)
	restart = input("Want to play again? Yes(Y)/No(N): ").upper()
	if restart == "Y":
		os.system('cls')
		time.sleep(1)
	else:
		print()
		print("Thanks for Playing! ")
		break
