import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER, HORIZONTAL
from ai import ai_board
import time
from user_board import user_board


# Method to load a randomly generated board and solve it with AI
def start_ai_based():
    time.sleep(0.5)
    ai_option_button.destroy()
    user_option_button.destroy()
    time.sleep(1)
    Loading_lbl = tk.Label(game_frame, text="Generating Board .... ")
    Loading_lbl.place(relx=0.5, rely=0.45, anchor=CENTER)
    progress_bar.place(relx=0.5, rely=0.50, anchor=CENTER)
    for i in range(10):
        progress_bar['value'] += 10
        game_frame.update()
        time.sleep(0.5)
    game_frame.destroy()
    ai = ai_board()
    ai.place_ships()
    ai.board_frame.update()
    time.sleep(0.5)
    while True:
        ai.attack_guess()
        time.sleep(0.8)
        ai.board_frame.update()
        if ai.check_for_win() == 17:
            break
    time.sleep(0.5)
    win_alert = tk.Label(ai.board_frame, text=f'BOARD HAS BEEN DEFEATED {ai.attack_counter} ATTACKS')
    win_alert.pack()
    win_alert.place(x=50, y=50, width=550, height=550)
    ai.board_frame.mainloop()


# Method to Allow user to generate a board to be solved by AI
def start_user_based():
    time.sleep(1)
    game_frame.destroy()
    player = user_board()
    player.place_carrier()
    player.place_battleship()
    player.place_cruiser()
    player.place_submarine()
    player.place_destroyer()


game_frame = tk.Tk()
game_frame.title("Battle-Ship Solver")
game_frame.geometry("550x550")

progress_bar = ttk.Progressbar(game_frame, orient=HORIZONTAL, length=300, mode='determinate')

ai_option_button = tk.Button(game_frame, text="Solve A Randomly Generated Board", command=start_ai_based)
ai_option_button.place(relx=0.5, rely=0.45, anchor=CENTER)

user_option_button = tk.Button(game_frame, text="Solve A Board Created By Me", command=start_user_based)
user_option_button.place(relx=0.5, rely=0.5, anchor=CENTER)

game_frame.mainloop()
