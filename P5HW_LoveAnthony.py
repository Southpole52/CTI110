#Anthony Love
#5/5/2024
#P5HW_LoveAnthony
#User Defined Functions

import random


def main():
    while True:
        print("Welcome to Math Quiz")
        print()
        print("Main Menu")
        print("---------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        print()
        choice = input("Please choose one of the menu options: ")
        if choice == "1":
            addition()
        elif choice == "2":
            subtraction()
        elif choice == "3":
            print("Thank you for playing...")
            print("BYE!!")
            break
        else:
            print("Invalid Choice. Please enter 1, 2, or 3 ")
        
    
    



def addition():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f" {num1}")
    print(f"+{num2}")
    correct = num1 + num2
    guesses = 0
    while True:
        answer = int(input("Enter Answer."))
        guesses += 1
        if answer == correct:
            print("Congratulations!!!! Your Answer is correct")
            print(f"Number of guesses: {guesses}")
            print()
            break
        elif answer < correct:
            print()
            print("Sorry, guess is too low.")
        else:
            print()
            print("Sorry, guess is too high.")

    
def subtraction():
    num3 = random.randint(1, 100)
    num4 = random.randint(1, 100)
    print(f" {num3}")
    print(f"-{num4}")
    correct = num3 - num4
    guesses = 0
    while True:
        answer = int(input("Enter Answer."))
        guesses += 1
        if answer == correct:
            print("Congratulations!!!! Your Answer is correct")
            print(f"Number of guesses: {guesses}")
            print()
            break
        elif answer < correct:
            print()
            print("Sorry, guess is too low.")
        else:
            print()
            print("Sorry, guess is too high.")

main()







