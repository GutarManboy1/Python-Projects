#Number Guessing Game#
#
#Have the computer generate a random number between 1 and 100.
#The user will then guess what the number is.
#The user has 10 chances to guess the correct number.
#If the user guesses the correct number, the program will print "You got it, buttcheeks!"
#If the user guesses too high, the program will print "Too high, butthead!"
#If the user guesses too low, the program will print "Too low, pinhead!"
#If the user runs out of guesses, the program will print "Sorry, you lose!"
#
import random

while True:
    secret_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100. Try to guess it.")

    for i in range(1, 11):
        guess = int(input(f"Guess #{i}: "))
        if guess == secret_number:
            print("You got it, buttcheeks!")
            break
        elif guess > secret_number:
            print("Too high, butthead!")
        elif guess < secret_number:
            print("Too low, pinhead!")