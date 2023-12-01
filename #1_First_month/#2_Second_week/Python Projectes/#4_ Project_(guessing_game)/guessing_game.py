import random

def guess_number_game():
    play_again = "yes"  # Indicates if the user wants to play again
    total_wins = 0  # Variable to track the total number of wins
    total_losses = 0  # Variable to track the total number of losses

    while play_again.lower() == "yes":  # Main loop of the game runs as long as the user wants to play again
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 5. Try to guess it!")

        secret_number = random.randint(1, 5)  # Choosing a random number between 1 and 5
        attempts = 0  # Number of attempts for each round of the game
        guessed_correctly = False  # Set to check if the user guessed the correct number

        while attempts < 5:  # Sub-loop runs for a maximum of 5 attempts to guess the number
            try:
                user_guess = int(input("Enter your guess: "))  # Receiving user's guess
                attempts += 1  # Increasing the number of attempts by one

                if user_guess == secret_number:  # Checking the correctness of the guess
                    print("Congratulations! You guessed the correct number!")
                    total_wins += 1  # Increasing the number of wins by one
                    guessed_correctly = True
                    break
                else:
                    if attempts < 5:  # Making sure the user has more attempts before giving a hint
                        hint_response = input("Incorrect guess! Do you want a hint? (yes/no): ")
                        if hint_response.lower() == "yes":
                            if user_guess < secret_number:
                                print("Try a higher number!")
                            else:
                                print("Try a lower number!")
                    else:
                        print("Sorry, you've used all your attempts. The correct number was:", secret_number)
                        total_losses += 1  # Increasing the number of losses by one
            except ValueError:
                print("Please enter a valid number.")

        if not guessed_correctly:  # If the guess wasn't correct, ask the user if they want to play again
            play_again = input("Do you want to play again? (yes/no): ")
        else:
            play_again = input("Do you want to play again? (yes/no): ")

    # Displaying results once the game is over
    print("Game Over!")
    print(f"Total Wins: {total_wins}")
    print(f"Total Losses: {total_losses}")
    print("Thanks for playing! Goodbye!")

    guess_number_game()  # Calling the function to start the game
