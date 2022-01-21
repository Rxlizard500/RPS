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