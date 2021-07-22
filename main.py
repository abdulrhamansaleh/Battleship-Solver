import time
import tkinter as tk
from ai_board import ai_board

ai = ai_board()
ai.place_ships()
ai.board_frame.update()
time.sleep(1)
attack_counter = 0

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
