import random

def get_user_choice():
    # Loop until the user enters a valid choice
    while True:
        user_choice = input("Enter Rock, Paper, or Scissors: ").capitalize()
        # Check if the user's choice is valid
        if user_choice in ['Rock', 'Paper', 'Scissors']:
            return user_choice
        # If the choice is not valid, inform the user and loop again
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")

def play_game():
    # Define the possible choices
    choices = ['Rock', 'Paper', 'Scissors']
    # Get the user's choice
    user_choice = get_user_choice()
    # Generate a random choice for the computer
    computer_choice = random.choice(choices)
    # Print the choices
    print(f"You chose {user_choice}. Computer chose {computer_choice}.")

    # Determine the winner based on the choices
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice, computer_choice) in [('Rock', 'Scissors'), ('Paper', 'Rock'), ('Scissors', 'Paper')]:
        result = "You win!"
    else:
        result = "Computer wins!"

    # Print the result
    print(result)

if __name__ == "__main__":
    # Start the game
    play_game()
