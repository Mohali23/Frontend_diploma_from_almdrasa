# Import necessary libraries
import tkinter as tk  # Tkinter for GUI
import random  # For random player selection

# Function to handle the next player's turn
def next_player(row, col):
    global player
    if grid_btns[row][col]['text'] == "" and check_winner() == False:
        # Human player's turn
        grid_btns[row][col]['text'] = "X"

        if check_winner() == False:
            message_label.config(text=(players[1] + " turn"))  # Assuming 'o' is the computer

            # Computer's turn after human player
            root.after(1000, computer_turn)

        elif check_winner() == True:
            message_label.config(text=(players[0] + " wins!"))
            update_score(players[0])

        elif check_winner() == 'tie':
            message_label.config(text=("Tie, No Winner!"))


def computer_turn():
    if check_winner() == False:
        empty_cells = [(row, col) for row in range(3) for col in range(3) if grid_btns[row][col]['text'] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            grid_btns[row][col]['text'] = players[1]  # Assuming 'o' represents the computer's move

            if check_winner() == False:
                message_label.config(text=(players[0] + " turn"))

            elif check_winner() == True:
                message_label.config(text=(players[1] + " wins!"))
                update_score(players[1])

            elif check_winner() == 'tie':
                message_label.config(text=("Tie, No Winner!"))


# Function to check if there's a winner
def check_winner():
    global game_finished  # Global variable
    # Check rows for a winning combination
    for row in range(3):
        if grid_btns[row][0]['text'] == grid_btns[row][1]['text'] == grid_btns[row][2]['text'] != "":
            highlight_winner_buttons([(row, 0), (row, 1), (row, 2)])  # Highlight winning buttons
            game_finished = True  # Game is finished
            return True  # Return True for a winner

    # Check columns for a winning combination
    for col in range(3):
        if grid_btns[0][col]['text'] == grid_btns[1][col]['text'] == grid_btns[2][col]['text'] != "":
            highlight_winner_buttons([(0, col), (1, col), (2, col)])  # Highlight winning buttons
            game_finished = True  # Game is finished
            return True  # Return True for a winner

    # Check diagonals for a winning combination
    if grid_btns[0][0]['text'] == grid_btns[1][1]['text'] == grid_btns[2][2]['text'] != "":
        highlight_winner_buttons([(0, 0), (1, 1), (2, 2)])  # Highlight winning buttons
        game_finished = True  # Game is finished
        return True  # Return True for a winner

    elif grid_btns[0][2]['text'] == grid_btns[1][1]['text'] == grid_btns[2][0]['text'] != "":
        highlight_winner_buttons([(0, 2), (1, 1), (2, 0)])  # Highlight winning buttons
        game_finished = True  # Game is finished
        return True  # Return True for a winner

    # Check for a tie
    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                grid_btns[row][col].config(bg='red')  # Set button color to red
        game_finished = True  # Game is finished
        return 'tie'  # Return 'tie' for a tie
    else:
        return False  # Return False if the game is ongoing


# Function to check for empty spaces on the board
def check_empty_spaces():
    spaces = 9  # Total spaces on the board
    for row in range(3):
        for col in range(3):
            if grid_btns[row][col]['text'] != "":
                spaces -= 1  # Decrement spaces for filled buttons
    return spaces != 0  # Return True if there are empty spaces, False otherwise


# Function to start a new game
def start_new_game():
    global player, game_finished  # Global variables
    player = random.choice(players)  # Randomly select the starting player
    message_label.config(text=(player + " turn"))  # Display starting player's turn
    game_finished = False  # Reset game status to not finished

    # Reset all buttons on the board
    for row in range(3):
        for col in range(3):
            grid_btns[row][col].config(text="", bg="#F0F0F0", state=tk.NORMAL)


# Function to quit the game
def quit_game():
    root.destroy()  # Destroy the Tkinter window


# Function to update the score for the winner
def update_score(winner):
    if winner == players[0]:
        player_X_score_label.config(text=str(int(player_X_score_label["text"]) + 1))  # Update Player X's score
    else:
        player_O_score_label.config(text=str(int(player_O_score_label["text"]) + 1))  # Update Player O's score


# Function to highlight the winning buttons
def highlight_winner_buttons(buttons_to_highlight):
    for row, col in buttons_to_highlight:
        grid_btns[row][col].config(bg="green")  # Highlight winning buttons


# Players and initial setup
players = ["X", "O"]
player = random.choice(players)  # Randomly choose the starting player
player_X_score = 0
player_O_score = 0
game_finished = False  # Flag to track game status

# Set font details
font_family = 'Arial'
font_size = 50

# Create Tkinter window
root = tk.Tk()

# Window size and title
window_width = 600
window_height = 600

# Retrieve screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate screen coordinates for window placement
screen_coordinate_x = (screen_width // 2) - (window_width // 2)
screen_coordinate_y = (screen_height // 2) - (window_height // 2)

root.geometry(f'{window_width}x{window_height}+{screen_coordinate_x}+{screen_coordinate_y}')
root.title('Tic_Tac_Toe__Game from Almdrasa')

# Configure window layout
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=8)
root.columnconfigure(0, weight=1)

# Frame for displaying scores
score_frame = tk.Frame(root)
score_frame.grid(row=0, column=0, sticky='nesw')
score_frame.columnconfigure(0, weight=1)
score_frame.columnconfigure(1, weight=1)

# Labels for Player X's score and name
player_X_score_label = tk.Label(score_frame, text='0', font=(font_family, font_size))
player_X_score_label.grid(row=0, column=0, sticky='nesw')

playerX_name_label = tk.Label(score_frame, text='(X) Mohali Score', font=(font_family, 15))
playerX_name_label.grid(row=1, column=0, sticky='nesw')

# Labels for Player O's score and name
player_O_score_label = tk.Label(score_frame, text='0', font=(font_family, font_size))
player_O_score_label.grid(row=0, column=1, sticky='nesw')

playerO_name_label = tk.Label(score_frame, text='(O) Almdrasa Score', font=(font_family, 15))
playerO_name_label.grid(row=1, column=1, sticky='nesw')

# Label to display game messages
message_label = tk.Label(root, text=(player + ' turn'), font=(font_family, 15))
message_label.grid(row=1, column=0, sticky='nesw')

# Frame for the game grid
game_place_frame = tk.Frame(root, borderwidth=2, relief='groove') 
game_place_frame.grid(row=2, column=0, sticky='nesw')

# Initialize grid buttons as a 2D array
grid_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Create and place buttons for the game grid
for row in range(3):
    game_place_frame.rowconfigure(row, weight=1)
    for col in range(3):
        game_place_frame.columnconfigure(col, weight=1)
        # Create buttons with click action linked to next_player function
        grid_btns[row][col] = tk.Button(game_place_frame, text="", font=(font_family, 50), width=4, height=1, command=lambda row=row, col=col: next_player(row, col))
        grid_btns[row][col].grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Frame for game controls
control_place_frame = tk.Frame(root)
control_place_frame.grid(row=3, column=0, sticky='s')

# Buttons to restart or quit the game
btn_restart_game = tk.Button(control_place_frame, text='Restart Game', font=(font_family, 15), command=start_new_game)
btn_restart_game.grid(row=0, column=0)

btn_quit_game = tk.Button(control_place_frame, text='Quit Game', font=(font_family, 15), command=quit_game)
btn_quit_game.grid(row=0, column=1)

# Run the Tkinter main loop
root.mainloop()
