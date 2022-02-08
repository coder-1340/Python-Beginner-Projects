'''
Fizz_Buzz
Created By: Punascha Das'''

import time

def fizz_buzz(num):
    if num == 0:
        print('Input should be non-zero number')
    elif num % 15 == 0:
        print('fizz_buzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print('Invalid')


'''
Palindrome_Checker
Created By: Punascha Das'''

def palindrome(word):
    start = 0
    front = ''
    length = len(word)
    last = ''
    mid = (length // 2) + 1
    if length <= 1:
        print("Input should be of at least 2 letters")
    else: 
        for index in range(mid):
            front = word[start]
            last = word[length - 1]
            if front == last:
                start += 1
                length -= 1
            else:
                print("It is not a  palindrome")
                break
        if front == last:
            print('It is a palindrome')


print('FIZZ BUZZ:')
time.sleep(1)
fizz_buzz(int(input('Enter a number: ')))
time.sleep(1)
print('\nPALINDROME CHECKER:')
time.sleep(1)
palindrome(input("Enter a word: "))
