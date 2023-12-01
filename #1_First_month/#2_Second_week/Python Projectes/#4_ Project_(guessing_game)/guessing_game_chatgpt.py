import random
from tabulate import tabulate
from colorama import init, Fore

init(autoreset=True)

def guess_number_game():
    play_again = "yes"
    total_wins = 0
    total_losses = 0
    results = []

    while play_again.lower() == "yes":
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 5. Try to guess it!")

        secret_number = random.randint(1, 5)
        attempts = 0
        guessed_correctly = False

        while attempts < 5:
            try:
                user_guess = int(input("Enter your guess: "))
                attempts += 1

                if user_guess == secret_number:
                    print(Fore.GREEN + "Congratulations! You guessed the correct number!")
                    total_wins += 1
                    guessed_correctly = True
                    results.append("Win")
                    break
                else:
                    if attempts < 5:
                        hint_response = input("Incorrect guess!" + " Do you want a hint? (yes/no): ")
                        if hint_response.lower() == "yes":
                            if user_guess < secret_number:
                                print("Try a higher number!")
                            else:
                                print("Try a lower number!")
                        elif hint_response.lower() != "no":
                            print("Please enter 'yes' or 'no' only.")  # Error message for invalid input
                    else:
                        print(Fore.RED + f"Sorry, you've used all your attempts. The correct number was: {secret_number}")
                        total_losses += 1
                        guessed_correctly = False
                        results.append("Loss")
            except ValueError:
                print("Please enter a valid number.")

        if not guessed_correctly:
            play_again = input("Do you want to play again? (yes/no): ")
            while play_again.lower() not in ["yes", "no"]:
                print("Please enter 'yes' or 'no' only.")  # Error message for invalid input
                play_again = input("Do you want to play again? (yes/no): ")
        else:
            play_again = input("Do you want to play again? (yes/no): ")
            while play_again.lower() not in ["yes", "no"]:
                print("Please enter 'yes' or 'no' only.")  # Error message for invalid input
                play_again = input("Do you want to play again? (yes/no): ")

    print("\nGame Over!")
    print("Here are the results:")
    table = [["Wins", total_wins], ["Losses", total_losses]]
    headers = ["Result", "Count"]
    print(tabulate(table, headers=headers, tablefmt="grid"))

guess_number_game()
