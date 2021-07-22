from tkinter import *
import tkinter as tk
from tkinter.constants import CENTER


game_frame = tk.Tk()
game_frame.title("Battle-Ship Solver")
game_frame.geometry("550x550")



ai_option_button = tk.Button(game_frame,text="Solve A Randomly Generated Board")
ai_option_button.place(relx= 0.5,rely= 0.45,anchor=CENTER)
user_option_button = tk.Button(game_frame,text="Solve A Board Created By Me")
user_option_button.place(relx= 0.5,rely= 0.5,anchor=CENTER)
game_frame.mainloop()
