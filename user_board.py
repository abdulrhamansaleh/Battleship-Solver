import time
import tkinter as tk
from random import randrange
from tkinter import DISABLED


def _input_(text):
    letter_input = text[0:1].upper()
    number_input = int(text[1:])
    row_val = 0
    col_val = number_input * 50
    if letter_input == 'A':
        row_val = 50
    elif letter_input == 'B':
        row_val = 100
    elif letter_input == 'C':
        row_val = 150
    elif letter_input == 'D':
        row_val = 200
    elif letter_input == 'E':
        row_val = 250
    elif letter_input == 'F':
        row_val = 300
    elif letter_input == 'G':
        row_val = 350
    elif letter_input == 'H':
        row_val = 400
    elif letter_input == 'I':
        row_val = 450
    elif letter_input == 'J':
        row_val = 500
    return row_val, col_val


class user_board:
    def __init__(self):
        # LETTER AND NUMBER LIST USED TO DISPLAY COORDINATE LIKE ROW AND COLUMN LABELS:
        self.attack_counter = 0
        self.continue_counter = 0
        self.win_counter = 0
        
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        # STORES COORDINATES FOR GRID IN A LIST
        self.cord_list = []
        
        # STORES BUTTONS OF GRID IN A DICTIONARY
        self.buttons_dict = {}
        
        # COUNTER VARIABLE USED TO TRACK AMOUNT OF SHIPS PLACED
        self.ship_counter = 0
        
        #  COUNTER TO ALLOW AI ATTACKING TURN
        self.ai_turn = 0
        self.player_turn = 0

        # MAIN FRAME SETUP:
        self.board_frame = tk.Tk()
        self.board_frame.title("Player Board")
        self.board_frame.geometry("1500x550")
        self.orientation_val = tk.IntVar()
        
        # CARRIER PLACEMENT DISPLAY:
        self.carrier_input = tk.Entry(self.board_frame, bg='white', fg='black')
        self.carrier_horizontal = tk.Radiobutton(self.board_frame, text="Horizontal", variable=self.orientation_val,
                                                 value=1)
        self.carrier_vertical = tk.Radiobutton(self.board_frame, text="Vertical", variable=self.orientation_val,
                                               value=0)
        
        # BATTLESHIP PLACEMENT DISPLAY:
        self.battleship_input = tk.Entry(self.board_frame, bg='white', fg='black')
        self.battleship_horizontal = tk.Radiobutton(self.board_frame, text="Horizontal", variable=self.orientation_val,
                                                    value=1)
        self.battleship_vertical = tk.Radiobutton(self.board_frame, text="Vertical", variable=self.orientation_val,
                                                  value=0)
        
        # CRUISER PLACEMENT DISPLAY:
        self.cruiser_input = tk.Entry(self.board_frame, bg='white', fg='black')
        self.cruiser_horizontal = tk.Radiobutton(self.board_frame, text="Horizontal", variable=self.orientation_val,
                                                 value=1)
        self.cruiser_vertical = tk.Radiobutton(self.board_frame, text="Vertical", variable=self.orientation_val,
                                               value=0)
        
        # SUBMARINE PLACEMENT DISPLAY:
        self.submarine_input = tk.Entry(self.board_frame, bg='white', fg='black')
        self.submarine_horizontal = tk.Radiobutton(self.board_frame, text="Horizontal", variable=self.orientation_val,
                                                   value=1)
        self.submarine_vertical = tk.Radiobutton(self.board_frame, text="Vertical", variable=self.orientation_val,
                                                 value=0)
        
        # DESTROYER PLACEMENT DISPLAY:
        self.destroyer_input = tk.Entry(self.board_frame, bg='white', fg='black')
        self.destroyer_horizontal = tk.Radiobutton(self.board_frame, text="Horizontal", variable=self.orientation_val,
                                                   value=1)
        self.destroyer_vertical = tk.Radiobutton(self.board_frame, text="Vertical", variable=self.orientation_val,
                                                 value=0)
        
        # LABEL FOR USER INSTRUCTION ON SHIP PLACEMENT:
        self.input_label = tk.Label(self.board_frame,
                                    text="Provide starting (letter)(number) for ship placement ex. a1 and Select "
                                         "orientation:",
                                    bg="black", fg="white")
        self.input_label.place(x=950, y=10, width=450, height=25)
        
        # Labels and graphic demonstration of carrier ship size relative to the board:
        self.carrier_lbl = tk.Label(self.board_frame, bg="black", text="Carrier", fg="white")
        self.carrier_lbl.place(x=575, y=55, width=50, height=30)
        self.carrier_ship = tk.Button(self.board_frame, bg="green", text="5 Long")
        self.carrier_ship.place(x=650, y=45, width=250, height=50)
        
        # Labels and graphic demonstration of battleship ship size relative to the board:
        self.battleship_lbl = tk.Label(self.board_frame, bg="black", text="Battleship", fg="white")
        self.battleship_lbl.place(x=565, y=155, width=70, height=30)
        self.battleship_ship = tk.Button(self.board_frame, bg="yellow", text="4 Long")
        self.battleship_ship.place(x=650, y=145, width=200, height=50)
        
        # Labels and graphic demonstration of cruiser ship size relative to the board:
        self.cruiser_lbl = tk.Label(self.board_frame, bg="black", text="Cruiser", fg="white")
        self.cruiser_lbl.place(x=575, y=255, width=50, height=30)
        self.cruiser_ship = tk.Button(self.board_frame, bg="orange", text="3 Long")
        self.cruiser_ship.place(x=650, y=245, width=150, height=50)
        
        # Labels and graphic demonstration of submarine ship size relative to the board:
        self.submarine_lbl = tk.Label(self.board_frame, bg="black", text="Submarine", fg="white")
        self.submarine_lbl.place(x=565, y=355, width=70, height=30)
        self.submarine_ship = tk.Button(self.board_frame, bg="red", text="3 Long")
        self.submarine_ship.place(x=650, y=345, width=150, height=50)
        
        # Labels and graphic demonstration of destroyer ship size relative to the board:
        self.destroyer_lbl = tk.Label(self.board_frame, bg="black", text="Destroyer", fg="white")
        self.destroyer_lbl.place(x=565, y=455, width=70, height=30)
        self.destroyer_ship = tk.Button(self.board_frame, bg="purple", text="2 Long")
        self.destroyer_ship.place(x=650, y=445, width=100, height=50)

        # CREATES MAIN BATTLESHIP BOARD
        for grid_row in range(50, 550, 50):
            for grid_col in range(50, 550, 50):
                self.coord = str(grid_row) + "_" + str(grid_col)
                self.cord_list.append(self.coord)
                self.buttons_dict[self.cord_list[-1]] = tk.Button(self.board_frame, bg="blue")
                self.buttons_dict[self.cord_list[-1]].place(x=grid_row, y=grid_col, width=50, height=50)

        # COLUMN COORDINATES FOR GRID
        for grid_row in range(50, 550, 50):
            counter = 0
            for i in range(10):
                ship_square = tk.Button(self.board_frame, bg="grey", fg="white", text=letter[i], state=DISABLED)
                ship_square.place(x=50 + counter, y=0, width=50, height=50)

                counter = counter + 50
                
        # ROW COORDINATES FOR GRID
        for grid_row in range(50, 550, 50):
            counter = 0
            for i in range(10):
                ship_square = tk.Button(self.board_frame, bg="grey", fg="white", text=number[i], state=DISABLED)
                ship_square.place(x=0, y=50 + counter, width=50, height=50)
                counter = counter + 50

    # RETURNS COUNTER THAT ACCOUNTS FOR NUMBER OF SHIPS SUNK
    def check_for_win(self):
        return self.win_counter

    # METHOD TO GUESS ACCORDING TO PREVIOUS GUESS
    def educated_hit_guess(self, row, col):
        # HORIZONTAL GUESS
        counter = 50
        try:
            for i in range(5):
                if self.buttons_dict[f'{row + counter}_{col}'].cget("text") == "   ":
                    self.buttons_dict[f'{row + counter}_{col}'].configure(state=DISABLED, bg="black",
                                                                          text="HIT")
                    self.win_counter = self.win_counter + 1
                    counter = counter + 50
            for i in range(5):
                if self.buttons_dict[f'{row}_{col + counter}'].cget("text") == "   ":
                    self.buttons_dict[f'{row}_{col + counter}'].configure(state=DISABLED, bg="black",
                                                                          text="HIT")
                    self.win_counter = self.win_counter + 1
                    counter = counter + 50
            for i in range(5):
                if self.buttons_dict[f'{row - counter}_{col}'].cget("text") == "   ":
                    self.buttons_dict[f'{row - counter}_{col}'].configure(state=DISABLED, bg="black",
                                                                          text="HIT")
                    self.win_counter = self.win_counter + 1
                    counter = counter + 50
            for i in range(5):
                if self.buttons_dict[f'{row}_{col - counter}'].cget("text") == "   ":
                    self.buttons_dict[f'{row}_{col - counter}'].configure(state=DISABLED, bg="black",
                                                                          text="HIT")
                    self.win_counter = self.win_counter + 1
                    counter = counter + 50
        except:
            self.attack_guess()

    def attack_guess(self):
        self.attack_counter = self.attack_counter + 1
        row_guess = randrange(50, 550, 50)
        col_guess = randrange(50, 550, 50)
        if self.buttons_dict[f'{row_guess}_{col_guess}'].cget("text") == "   ":
            self.buttons_dict[f'{row_guess}_{col_guess}'].configure(state=DISABLED, bg="black", text="HIT")
            self.win_counter = self.win_counter + 1
            self.educated_hit_guess(row_guess, col_guess)
        elif self.buttons_dict[f'{row_guess}_{col_guess}'].cget("bg") == "blue":
            self.buttons_dict[f'{row_guess}_{col_guess}'].configure(state=DISABLED, bg="white", text="MISS")
            self.educated_hit_guess(row_guess, col_guess)
        elif self.buttons_dict[f'{row_guess}_{col_guess}'].cget("text") == "MISS":
            self.attack_counter = self.attack_counter - 1

    # BEGINS GUESSING ALGORITHM TO SOLVE USER PROVIDED  BOARD
    def start_game(self):
        if self.ship_counter == 5:
            self.input_label.destroy()
            self.board_frame.geometry("550x550")
            while True:
                self.attack_guess()
                time.sleep(0.5)
                self.board_frame.update()
                if self.check_for_win() == 17:
                    break
            time.sleep(0.5)
            win_alert = tk.Label(self.board_frame, text=f'BOARD HAS BEEN DEFEATED {self.attack_counter} ATTACKS')
            win_alert.pack()
            win_alert.place(x=50, y=50, width=550, height=550)
            self.board_frame.mainloop()
            time.sleep(3)
            self.board_frame.destroy()

    # METHOD TO PLACE SHIPS ACCORDING TO SPECIFIED SHIP CONSTRAINTS
    def placing_ships(self, board_row, board_col, ship_orientation, ship_colour, iteration):
        counter = 50
        if ship_orientation == 1:
            self.buttons_dict[f'{board_row}_{board_col}'].configure(bg=f"{ship_colour}", text="   ")
            for i in range(iteration):
                self.buttons_dict[f'{board_row + counter}_{board_col}'].configure(bg=f"{ship_colour}", text="   ")
                counter = counter + 50
        elif ship_orientation == 0:
            self.buttons_dict[f'{board_row}_{board_col}'].configure(bg=f"{ship_colour}", text="   ")
            for i in range(iteration):
                self.buttons_dict[f'{board_row}_{board_col + counter}'].configure(bg=f"{ship_colour}", text="   ")
                counter = counter + 50

    # METHOD TO DISPLAY CARRIER PLACEMENT INTERFACE
    def place_carrier(self):
        self.carrier_input.place(x=955, y=55, width=45, height=30)
        self.carrier_horizontal.place(x=1100, y=55)
        self.carrier_vertical.place(x=1200, y=55)
        self.carrier_horizontal.configure(command=self.validate_carrier)
        self.carrier_vertical.configure(command=self.validate_carrier)

    # METHOD TO VALIDATE USER INPUT FOR CARRIER SHIP PLACEMENT
    def validate_carrier(self):
        
        try:
            
            # VARIABLES TO RETRIEVE TEXT AND ORIENTATION VALUES
            text = self.carrier_input.get()
            orientation = self.orientation_val.get()
    
            # CHECK HORIZONTAL AND VERTICAL OUT OF BOUNDS
            if orientation == 1 and _input_(text)[0] > 300 or (orientation == 0 and _input_(text)[1] > 300):
                invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIP IS OUT OF BOUNDS")
                invalid_label.place(x=955, y=55, width=450, height=50)
                self.board_frame.update()
                time.sleep(1)
                invalid_label.destroy()
                self.board_frame.update()
                
            #  IF INPUT IS NOT OUT OF BOUNDS CHECK IF IT OCCUPIED THE SPACE OF ANOTHER SHIP VERTICALLY
            elif orientation == 0 and _input_(text)[1] < 300:
                
                if self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1] + 50}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1] + 100}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1] + 150}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1] + 200}'].cget("bg") != "blue":
                    invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIPS ARE OVERLAPPING")
                    invalid_label.place(x=955, y=55, width=450, height=50)
                    self.board_frame.update()
                    time.sleep(1)
                    invalid_label.destroy()
                    self.board_frame.update()
                    
                else:
                    self.placing_ships(_input_(text)[0], _input_(text)[1], orientation, "green", 4)
                    self.board_frame.update()
                    self.carrier_vertical.destroy()
                    self.carrier_horizontal.destroy()
                    self.carrier_input.destroy()
                    self.carrier_ship.destroy()
                    self.carrier_lbl.destroy()
                    self.board_frame.update()
                    self.ship_counter = self.ship_counter + 1
                    self.start_game()
                    
            # IF INPUT IS NOT OUT OF BOUNDS HORIZONTALLY CHECK IF IT OCCUPIES SPACE OF ANOTHER SHIP HORIZONTALLY
            elif orientation == 1 and _input_(text)[0] < 300:
                
                if self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0] + 50}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0] + 100}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0] + 150}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0] + 200}_{_input_(text)[1]}'].cget("bg") != "blue":
                    invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIPS ARE OVERLAPPING")
                    invalid_label.place(x=955, y=55, width=450, height=50)
                    self.board_frame.update()
                    time.sleep(1)
                    invalid_label.destroy()
                    self.board_frame.update()
                    
                else:
                    self.placing_ships(_input_(text)[0], _input_(text)[1], orientation, "green", 4)
                    self.board_frame.update()
                    self.carrier_vertical.destroy()
                    self.carrier_horizontal.destroy()
                    self.carrier_input.destroy()
                    self.carrier_ship.destroy()
                    self.carrier_lbl.destroy()
                    self.board_frame.update()
                    self.ship_counter = self.ship_counter + 1
                    self.start_game()
                    
        except Exception:
            invalid_label = tk.Label(self.board_frame, text="INVALID INPUT")
            invalid_label.place(x=955, y=55, width=450, height=50)
            self.board_frame.update()
            time.sleep(1)
            invalid_label.destroy()
            self.board_frame.update()

    # METHOD TO DISPLAY BATTLESHIP PLACEMENT INTERFACE
    def place_battleship(self):
        self.battleship_input.place(x=955, y=155, width=45, height=30)
        self.battleship_horizontal.place(x=1100, y=155)
        self.battleship_vertical.place(x=1200, y=155)
        self.battleship_horizontal.configure(command=self.validate_battleship)
        self.battleship_vertical.configure(command=self.validate_battleship)

    # METHOD TO VALIDATE USER INPUT FOR BATTLESHIP SHIP PLACEMENT
    def validate_battleship(self, *args):
        
        try:
            
            # VARIABLES TO RETRIEVE TEXT AND ORIENTATION VALUES
            text = self.battleship_input.get()
            orientation = self.orientation_val.get()
            
            # CHECK HORIZONTAL AND VERTICAL OUT OF BOUNDS
            if orientation == 1 and _input_(text)[0] > 350 or (orientation == 0 and _input_(text)[1] > 350):
                invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIP IS OUT OF BOUNDS")
                invalid_label.place(x=955, y=155, width=450, height=50)
                self.board_frame.update()
                time.sleep(1)
                invalid_label.destroy()
                self.board_frame.update()
                
            #  IF INPUT IS NOT OUT OF BOUNDS CHECK IF IT OCCUPIED THE SPACE OF ANOTHER SHIP VERTICALLY
            elif orientation == 0 and _input_(text)[1] < 350:
                
                if self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1] + 50}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1] + 100}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1] + 150}'].cget("bg") != "blue":
                    invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIPS ARE OVERLAPPING")
                    invalid_label.place(x=955, y=155, width=450, height=50)
                    self.board_frame.update()
                    time.sleep(1)
                    invalid_label.destroy()
                    self.board_frame.update()
                    
                else:
                    self.placing_ships(_input_(text)[0], _input_(text)[1], orientation, "yellow", 3)
                    self.board_frame.update()
                    self.battleship_vertical.destroy()
                    self.battleship_horizontal.destroy()
                    self.battleship_input.destroy()
                    self.battleship_ship.destroy()
                    self.battleship_lbl.destroy()
                    self.board_frame.update()
                    self.ship_counter = self.ship_counter + 1
                    self.start_game()
                    
            # IF INPUT IS NOT OUT OF BOUNDS HORIZONTALLY CHECK IF IT OCCUPIES SPACE OF ANOTHER SHIP HORIZONTALLY
            elif orientation == 1 and _input_(text)[0] < 350:
                
                if self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0] + 50}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0] + 100}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0] + 150}_{_input_(text)[1]}'].cget("bg") != "blue":
                    invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIPS ARE OVERLAPPING")
                    invalid_label.place(x=955, y=155, width=450, height=50)
                    self.board_frame.update()
                    time.sleep(1)
                    invalid_label.destroy()
                    self.board_frame.update()
                    
                else:
                    self.placing_ships(_input_(text)[0], _input_(text)[1], orientation, "yellow", 3)
                    self.board_frame.update()
                    self.battleship_vertical.destroy()
                    self.battleship_horizontal.destroy()
                    self.battleship_input.destroy()
                    self.battleship_lbl.destroy()
                    self.battleship_ship.destroy()
                    self.board_frame.update()
                    self.ship_counter = self.ship_counter + 1
                    self.start_game()
                    
        except Exception:
            invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIP IS OUT OF BOUNDS")
            invalid_label.place(x=955, y=155, width=450, height=50)
            self.board_frame.update()
            time.sleep(1)
            invalid_label.destroy()
            self.board_frame.update()

    # METHOD TO DISPLAY CRUISER PLACEMENT INTERFACE
    def place_cruiser(self):
        self.cruiser_input.place(x=955, y=255, width=45, height=30)
        self.cruiser_horizontal.place(x=1100, y=255)
        self.cruiser_vertical.place(x=1200, y=255)
        self.cruiser_vertical.configure(command=self.validate_cruiser)
        self.cruiser_horizontal.configure(command=self.validate_cruiser)

    # METHOD TO VALIDATE USER INPUT FOR CRUISER SHIP PLACEMENT
    def validate_cruiser(self, *args):
        
        try:
            
            # VARIABLES TO RETRIEVE TEXT AND ORIENTATION VALUES
            text = self.cruiser_input.get()
            orientation = self.orientation_val.get()
            
            # CHECK HORIZONTAL AND VERTICAL OUT OF BOUNDS
            if orientation == 1 and _input_(text)[0] > 400 or (orientation == 0 and _input_(text)[1] > 400):
                invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIP IS OUT OF BOUNDS")
                invalid_label.place(x=955, y=255, width=450, height=50)
                self.board_frame.update()
                time.sleep(1)
                invalid_label.destroy()
                self.board_frame.update()
                
            #  IF INPUT IS NOT OUT OF BOUNDS CHECK IF IT OCCUPIED THE SPACE OF ANOTHER SHIP VERTICALLY
            elif orientation == 0 and _input_(text)[1] < 400:
                
                if self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1] + 50}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1] + 100}'].cget("bg") != "blue":
                    invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIPS ARE OVERLAPPING")
                    invalid_label.place(x=955, y=255, width=450, height=50)
                    self.board_frame.update()
                    time.sleep(1)
                    invalid_label.destroy()
                    self.board_frame.update()
                    
                else:
                    self.placing_ships(_input_(text)[0], _input_(text)[1], orientation, "orange", 2)
                    self.board_frame.update()
                    self.cruiser_vertical.destroy()
                    self.cruiser_horizontal.destroy()
                    self.cruiser_input.destroy()
                    self.cruiser_ship.destroy()
                    self.cruiser_lbl.destroy()
                    self.board_frame.update()
                    self.ship_counter = self.ship_counter + 1
                    self.start_game()
                    
            # IF INPUT IS NOT OUT OF BOUNDS HORIZONTALLY CHECK IF IT OCCUPIES SPACE OF ANOTHER SHIP HORIZONTALLY
            elif orientation == 1 and _input_(text)[0] < 400:
                
                if self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0] + 50}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0] + 100}_{_input_(text)[1]}'].cget("bg") != "blue":
                    invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIPS ARE OVERLAPPING")
                    invalid_label.place(x=955, y=255, width=450, height=50)
                    self.board_frame.update()
                    time.sleep(1)
                    invalid_label.destroy()
                    self.board_frame.update()
                    
                else:
                    self.placing_ships(_input_(text)[0], _input_(text)[1], orientation, "orange", 2)
                    self.board_frame.update()
                    self.cruiser_vertical.destroy()
                    self.cruiser_horizontal.destroy()
                    self.cruiser_input.destroy()
                    self.cruiser_ship.destroy()
                    self.cruiser_lbl.destroy()
                    self.board_frame.update()
                    self.ship_counter = self.ship_counter + 1
                    self.start_game()
                    
        except Exception:
            invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIP IS OUT OF BOUNDS")
            invalid_label.place(x=955, y=255, width=450, height=50)
            self.board_frame.update()
            time.sleep(1)
            invalid_label.destroy()
            self.board_frame.update()

    # METHOD TO DISPLAY SUBMARINE PLACEMENT INTERFACE
    def place_submarine(self):
        self.submarine_input.place(x=955, y=355, width=45, height=30)
        self.submarine_horizontal.place(x=1100, y=355)
        self.submarine_vertical.place(x=1200, y=355)
        self.submarine_horizontal.configure(command=self.validate_submarine)
        self.submarine_vertical.configure(command=self.validate_submarine)

    # METHOD TO VALIDATE USER INPUT FOR SUBMARINE SHIP PLACEMENT
    def validate_submarine(self, *args):
        
        try:
            
            # VARIABLES TO RETRIEVE TEXT AND ORIENTATION VALUES
            text = self.submarine_input.get()
            orientation = self.orientation_val.get()
            
            # CHECK HORIZONTAL AND VERTICAL OUT OF BOUNDS
            if orientation == 1 and _input_(text)[0] > 400 or (orientation == 0 and _input_(text)[1] > 400):
                invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIP IS OUT OF BOUNDS")
                invalid_label.place(x=955, y=355, width=450, height=50)
                self.board_frame.update()
                time.sleep(1)
                invalid_label.destroy()
                self.board_frame.update()
                
            #  IF INPUT IS NOT OUT OF BOUNDS CHECK IF IT OCCUPIED THE SPACE OF ANOTHER SHIP VERTICALLY
            elif orientation == 0 and _input_(text)[1] < 400:
                
                if self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1] + 50}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1] + 100}'].cget("bg") != "blue":
                    invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIPS ARE OVERLAPPING")
                    invalid_label.place(x=955, y=355, width=450, height=50)
                    self.board_frame.update()
                    time.sleep(1)
                    invalid_label.destroy()
                    self.board_frame.update()
                    
                else:
                    self.placing_ships(_input_(text)[0], _input_(text)[1], orientation, "red", 2)
                    self.board_frame.update()
                    self.submarine_vertical.destroy()
                    self.submarine_horizontal.destroy()
                    self.submarine_input.destroy()
                    self.submarine_lbl.destroy()
                    self.submarine_ship.destroy()
                    self.board_frame.update()
                    self.ship_counter = self.ship_counter + 1
                    self.start_game()
                    
            # IF INPUT IS NOT OUT OF BOUNDS HORIZONTALLY CHECK IF IT OCCUPIES SPACE OF ANOTHER SHIP HORIZONTALLY
            elif orientation == 1 and _input_(text)[0] < 400:
                
                if self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0] + 50}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0] + 100}_{_input_(text)[1]}'].cget("bg") != "blue":
                    invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIPS ARE OVERLAPPING")
                    invalid_label.place(x=955, y=355, width=450, height=50)
                    self.board_frame.update()
                    time.sleep(1)
                    invalid_label.destroy()
                    self.board_frame.update()
                    
                else:
                    self.placing_ships(_input_(text)[0], _input_(text)[1], orientation, "red", 2)
                    self.board_frame.update()
                    self.submarine_vertical.destroy()
                    self.submarine_horizontal.destroy()
                    self.submarine_input.destroy()
                    self.submarine_lbl.destroy()
                    self.submarine_ship.destroy()
                    self.board_frame.update()
                    self.ship_counter = self.ship_counter + 1
                    self.start_game()
                    
        except Exception:
            invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIP IS OUT OF BOUNDS")
            invalid_label.place(x=955, y=355, width=450, height=50)
            self.board_frame.update()
            time.sleep(1)
            invalid_label.destroy()
            self.board_frame.update()

    # METHOD TO DISPLAY DESTROYER PLACEMENT INTERFACE
    def place_destroyer(self):
        self.destroyer_input.place(x=955, y=455, width=45, height=30)
        self.destroyer_horizontal.place(x=1100, y=455)
        self.destroyer_vertical.place(x=1200, y=455)
        self.destroyer_horizontal.configure(command=self.validate_destroyer)
        self.destroyer_vertical.configure(command=self.validate_destroyer)

    # METHOD TO VALIDATE DESTROYER SHIP PLACEMENT
    def validate_destroyer(self, *args):
        
        try:
            # VARIABLES TO RETRIEVE TEXT AND ORIENTATION VALUES
            text = self.destroyer_input.get()
            orientation = self.orientation_val.get()
            
            # CHECK HORIZONTAL AND VERTICAL OUT OF BOUNDS
            if orientation == 1 and _input_(text)[0] > 450 or (orientation == 0 and _input_(text)[1] > 450):
                invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIP IS OUT OF BOUNDS")
                invalid_label.place(x=955, y=455, width=450, height=50)
                self.board_frame.update()
                time.sleep(1)
                invalid_label.destroy()
                self.board_frame.update()
                
            #  IF INPUT IS NOT OUT OF BOUNDS CHECK IF IT OCCUPIED THE SPACE OF ANOTHER SHIP VERTICALLY
            elif orientation == 0 and _input_(text)[1] < 450:
                
                if self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1] + 50}'].cget("bg") != "blue":
                    invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIPS ARE OVERLAPPING")
                    invalid_label.place(x=955, y=455, width=450, height=50)
                    self.board_frame.update()
                    time.sleep(1)
                    invalid_label.destroy()
                    self.board_frame.update()
                    
                else:
                    self.placing_ships(_input_(text)[0], _input_(text)[1], orientation, "purple", 1)
                    self.board_frame.update()
                    self.destroyer_vertical.destroy()
                    self.destroyer_horizontal.destroy()
                    self.destroyer_input.destroy()
                    self.destroyer_lbl.destroy()
                    self.destroyer_ship.destroy()
                    self.board_frame.update()
                    self.ship_counter = self.ship_counter + 1
                    self.start_game()
                    
            # IF INPUT IS NOT OUT OF BOUNDS HORIZONTALLY CHECK IF IT OCCUPIES SPACE OF ANOTHER SHIP HORIZONTALLY
            elif orientation == 1 and _input_(text)[0] < 450:
                
                if self.buttons_dict[f'{_input_(text)[0]}_{_input_(text)[1]}'].cget("bg") != "blue" \
                        or self.buttons_dict[f'{_input_(text)[0] + 50}_{_input_(text)[1]}'].cget("bg") != "blue":
                    invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIPS ARE OVERLAPPING")
                    invalid_label.place(x=955, y=455, width=450, height=50)
                    self.board_frame.update()
                    time.sleep(1)
                    invalid_label.destroy()
                    self.board_frame.update()
                    
                else:
                    self.placing_ships(_input_(text)[0], _input_(text)[1], orientation, "purple", 1)
                    self.board_frame.update()
                    self.destroyer_vertical.destroy()
                    self.destroyer_horizontal.destroy()
                    self.destroyer_input.destroy()
                    self.destroyer_lbl.destroy()
                    self.destroyer_ship.destroy()
                    self.board_frame.update()
                    self.ship_counter = self.ship_counter + 1
                    self.start_game()
                    
        except Exception:
            invalid_label = tk.Label(self.board_frame, text="TRY AGAIN SHIP IS OUT OF BOUNDS")
            invalid_label.place(x=955, y=455, width=450, height=50)
            self.board_frame.update()
            time.sleep(1)
            invalid_label.destroy()
            self.board_frame.update()
