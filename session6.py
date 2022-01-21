# Here are out imports

import random
import argparse

# Adds the '--rules' argument
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--rules", dest="rules", help="Prints the rules", action='store_true')
args = parser.parse_args()
# Checks if '--rules- or '-hr' was used
rulesSelected = bool(args.rules)

# Print rules if you type '--rules' or 'r'
if rulesSelected == True:
    print("######### RULES ########## \n" + "Here are the winning combinations for this game: \n"
          + "Rock vs Paper-> Paper wins \n"
          + "Rock vs Scissor-> Rock wins \n"
          + "Paper vs Scissor-> Scissor wins")
    quit()

goAgain = 0

# Sets 'user' wins to '0' by default
userWin = 0
# Sets 'computer' wins to '0' by default
compWin = 0
while True:
    print("Let's play!\n  Rock..\n    Paper..\n      Scissor..\n            SHOOT!")

    # initialize value of choice_name variable
    # corresponding to the choice value
    choice = random.randint(1, 3)
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
    # Condition for winning
    if((choice == 1 and comp_choice == 2) or
       (choice == 2 and comp_choice == 1)):
        print("Paper wins!\n ", end="")
        result = "paper"

    elif((choice == 1 and comp_choice == 3) or
         (choice == 3 and comp_choice == 1)):
        print("Rock wins!\n", end="")
        result = "Rock"
    else:
        print("Scissor wins!\n", end="")
        result = "scissor"