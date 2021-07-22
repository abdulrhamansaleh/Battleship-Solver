import tkinter as tk
from tkinter.constants import CENTER
from ai import ai_board
import time
from user_board import user_board

def start_ai_based():
    time.sleep(2)
    game_frame.destroy()
    ai = ai_board()
    ai.place_ships()
    ai.board_frame.update()
    time.sleep(1)
    while True:
        ai.attack_guess()
        time.sleep(0.5)
        ai.board_frame.update()
        if ai.check_for_win() == 17:
            break
    time.sleep(0.5)
    win_alert = tk.Label(ai.board_frame, text=f'BOARD HAS BEEN DEFEATED {ai.attack_counter} ATTACKS')
    win_alert.pack()
    win_alert.place(x=50, y=50, width=550, height=550)
    ai.board_frame.mainloop()

def start_user_based():
    time.sleep(2)
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

ai_option_button = tk.Button(game_frame, text="Solve A Randomly Generated Board", command=start_ai_based)
ai_option_button.place(relx=0.5, rely=0.45, anchor=CENTER)

user_option_button = tk.Button(game_frame, text="Solve A Board Created By Me",command=start_user_based)
user_option_button.place(relx=0.5, rely=0.5, anchor=CENTER)

game_frame.mainloop()
