import tkinter as tk
import random



def next_player(row, col):
    pass


players_name = ["Almdrasa", "Mohali"]
player = random.choice(players_name)

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

player_score_label = tk.Label(score_frame, text='0', font=(font_family, font_size))
player_score_label.grid(row=0, column=0, sticky='nesw')

player_name_label = tk.Label(score_frame, text='Almdrasa Score', font=(font_family, 15))
player_name_label.grid(row=1, column=0, sticky='nesw')


computer_score_label = tk.Label(score_frame, text='0', font=(font_family, font_size))
computer_score_label.grid(row=0, column=1, sticky='nesw')

computer_name_label = tk.Label(score_frame, text='Mohali Score', font=(font_family, 15))
computer_name_label.grid(row=1, column=1, sticky='nesw')

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

btn_restart_game = tk.Button(control_place_frame, text='Restart Game', font=(font_family, 15),)
btn_restart_game.grid(row=0, column=0)

btn_quit_game = tk.Button(control_place_frame, text='Quit Game', font=(font_family, 15),)
btn_quit_game.grid(row=0, column=1)


root.mainloop()