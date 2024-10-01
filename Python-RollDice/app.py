#ask for a roll (y/n)
#roll the dice
#display the result of the roll with 2 numbers
#if input is N, exit the program
#if input is not Y or N, give error message
import random

while True:
    roll = input("Would you like to roll the dice? (y/n) ").lower()
    if roll == "y":
        print("Rolling the dice...")
    
        print(random.randint(1, 6), random.randint(1, 6))
    elif roll == "n":
        print("Don't waste my time!")
        break
    else :
        print("Wrong input! Doofus!")