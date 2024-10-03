#Rock-Paper-Scissors#
#Ask the user Rock, Paper or Scissors? (r/p/s)#
#If the user enters a different answer, display an error message#
#If the user enters r, display "Rock"#
#If the user enters p, display "Paper"#
#If the user enters s, display "Scissors"#
#If the user enters r, p, or s, display "You win!"#

import random

while True:
    emojis = {"r": "🗿", "p": "📃", "s": "✂️"} # this is a dictionary, where you can store key:value pairs and have those values mapped ot those keys
    choices = ("r", "p", "s") #in this situation use a Tuple instead of a List to store multiple values. These values can not be changed.

    user_choice = input("Rock, Paper or Scissors? (r/p/s) ").lower()
    if user_choice not in choices:
        print("Invalid choice, dummy. Please try again.")
        continue

    computer_choice = random.choice(choices) #here that tuple is handed over as an argument

    #winning combinations for user
    if user_choice == "r" and computer_choice == "s":
        print(f"Your choice was {emojis[user_choice]} and the computer's choice was {emojis[computer_choice]}. You win!  ")
    elif user_choice == "p" and computer_choice == "r":
        print(f"Your choice is {emojis[user_choice]} and the computer's choice is {emojis[computer_choice]}. You win!  ")
    elif user_choice == "s" and computer_choice == "p":
        print(f"Your choice is {emojis[user_choice]} and the computer's choice is {emojis[computer_choice]}. You win!  ")
    #winning combinations for computer
    elif computer_choice == "r" and user_choice == "s":
        print(f"Your choice was {emojis[user_choice]} and the computer's choice was {emojis[computer_choice]}. You lose.  ")
    elif computer_choice == "p" and user_choice == "r":
        print(f"Your choice was {emojis[user_choice]} and the computer's choice was {emojis[computer_choice]}. You lose.  ")
    elif computer_choice == "s" and user_choice == "p":
        print(f"Your choice was {emojis[user_choice]} and the computer's choice was {emojis[computer_choice]}. You lose.  ")
    #tie
    elif user_choice == computer_choice:
        print("It's a tie.  ")
    continue

# there's an easier way to put all of these or statements together, all of the code above can now be done more quickly and readiably!!!!!!#
# if user_choice == computer_choice:
#     print("It's a tie.  ")
# elif (
#         (user_choice == "r" and computer_choice == "s") or
#         (user_choice == "p" and computer_choice == "r") or
#         (user_choice == "s" and computer_choice == "p")):
#     print ("You win! ")
# else:
#     print ("You lose, sucka! ")

# Remember the word continue is a reserved word in Python. You can not use it as a variable name.
#should_continue = input("Would you like to play again? (y/n) ")
# if should_continue == "y":
#     continue    
# else:
#     break