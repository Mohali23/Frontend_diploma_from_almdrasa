# Import random package from Pypi
import random

# list of play options
options = ["rock", "paper", "scissors"]

# Rinning rules
rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

# Get user choice 
player_choice = input("What's your choice? rock, paper, or scissors:")

# Get PC choice
computer_choice = random.choice(options)

# Print the choice of players on the screen
print("User played: " + player_choice)
print("Computer played: " + computer_choice)


# check the result 
if player_choice == computer_choice:
    print("It's a tie!")
elif rules.get(player_choice) == computer_choice:
    print("You win!")
else:
    print("You lose!")

