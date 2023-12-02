import tkinter as tk
import random

def next_player(row, col):
    global player
    if grid_btns[row][col]['text'] == "" and check_winner() == False:
        if player == players[0]:

            grid_btns[row][col]['text'] = player

            if check_winner() == False:

                player = players[1]
                message_label.config(text=(players[1] + " turn"))

            elif check_winner() == True:
                message_label.config(text=(players[0] + " wins!"))

            elif check_winner() == 'tie':
                message_label.config(text=("Tie, No Winner!"))

        elif player == players[1]:

            grid_btns[row][col]['text'] = player

            if check_winner() == False:

                player = players[0]
                message_label.config(text=(players[0] + " turn"))

            elif check_winner() == True:
                message_label.config(text=(players[1] + " wins!"))

            elif check_winner() == 'tie':
                message_label.config(text=("Tie, No Winner!"))


def check_winner():

    for row in range(3):
        if grid_btns[row][0]['text'] == grid_btns[row][1]['text'] == grid_btns[row][2]['text'] != "":
            grid_btns[row][0].config(bg="green")
            grid_btns[row][1].config(bg="green")
            grid_btns[row][2].config(bg="green")
            return True

    for col in range(3):
        if grid_btns[0][col]['text'] == grid_btns[1][col]['text'] == grid_btns[2][col]['text'] != "":
            grid_btns[0][col].config(bg="green")
            grid_btns[1][col].config(bg="green")
            grid_btns[2][col].config(bg="green")
            return True

    if grid_btns[0][0]['text'] == grid_btns[1][1]['text'] == grid_btns[2][2]['text'] != "":
        grid_btns[0][0].config(bg="green")
        grid_btns[1][1].config(bg="green")
        grid_btns[2][2].config(bg="green")
        return True
    elif grid_btns[0][2]['text'] == grid_btns[1][1]['text'] == grid_btns[2][0]['text'] != "":
        grid_btns[0][2].config(bg="green")
        grid_btns[1][1].config(bg="green")
        grid_btns[2][0].config(bg="green")
        return True
    
    winner = player

    # Update scores for players
    if winner == "X":
        player_X_score_label.config(text=str(int(player_X_score_label["text"]) + 1))
    else:
        player_O_score_label.config(text=str(int(player_O_score_label["text"]) + 1))

    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                grid_btns[row][col].config(bg='red')

        return 'tie'

    else:
        return False


def check_empty_spaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if grid_btns[row][col]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def start_new_game():
    global player
    player = random.choice(players)

    message_label.config(text=(player + " turn"))

    for row in range(3):
        for col in range(3):
            grid_btns[row][col].config(text="", bg="#F0F0F0")

def quit_game():
    root.destroy()


players = ["X", "O"]
player = random.choice(players)

font_family = 'Arial'
font_size = 50

root = tk.Tk()

window_width = 600
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

screen_coordinate_x = (screen_width // 2) - (window_width // 2)
screen_coordinate_y = (screen_height // 2) - (window_height // 2)

root.geometry(f'{window_width}x{window_height}+{screen_coordinate_x}+{screen_coordinate_y}')
root.title('Tic_Tac_Toe__Game from Almdrasa')
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=8)
root.columnconfigure(0, weight=1)


score_frame = tk.Frame(root)
score_frame.grid(row=0, column=0, sticky='nesw')
score_frame.columnconfigure(0, weight=1)
score_frame.columnconfigure(1, weight=1)

player_X_score_label = tk.Label(score_frame, text='0', font=(font_family, font_size))
player_X_score_label.grid(row=0, column=0, sticky='nesw')

playerX_name_label = tk.Label(score_frame, text='(X) Score', font=(font_family, 15))
playerX_name_label.grid(row=1, column=0, sticky='nesw')


player_O_score_label = tk.Label(score_frame, text='0', font=(font_family, font_size))
player_O_score_label.grid(row=0, column=1, sticky='nesw')

playerO_name_label = tk.Label(score_frame, text='(O) Score', font=(font_family, 15))
playerO_name_label.grid(row=1, column=1, sticky='nesw')

message_label = tk.Label(root, text=(player + ' turn'), font=(font_family, 15))
message_label.grid(row=1, column=0, sticky='nesw')

game_place_frame = tk.Frame(root, borderwidth=2, relief='groove') 
game_place_frame.grid(row=2, column=0, sticky='nesw')

grid_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for row in range(3):
    game_place_frame.rowconfigure(row, weight=1)
    for col in range(3):
        game_place_frame.columnconfigure(col, weight=1)
        grid_btns[row][col] = tk.Button(game_place_frame, text="", font=(font_family, 50), width=4, height=1, command=lambda row=row, col=col: next_player(row, col))
        grid_btns[row][col].grid(row=row, column=col, sticky="nsew", padx=5, pady=5)


control_place_frame = tk.Frame(root)
control_place_frame.grid(row=3, column=0, sticky='s')

btn_restart_game = tk.Button(control_place_frame, text='Restart Game', font=(font_family, 15), command=start_new_game)
btn_restart_game.grid(row=0, column=0)

btn_quit_game = tk.Button(control_place_frame, text='Quit Game', font=(font_family, 15), command=quit_game)
btn_quit_game.grid(row=0, column=1)


root.mainloop()