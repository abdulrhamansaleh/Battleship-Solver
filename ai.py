import time
from random import randrange
from tkinter import DISABLED, ttk, HORIZONTAL
import tkinter as tk


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


class ai_board:
    def __init__(self):
        # -GRAPHICAL ATTRIBUTES AND VARIABLES- #
        self.turn = 0
        self.attack_counter = 0
        self.win_counter = 0

        # LETTER AND NUMBER LIST USED TO DISPLAY COORDINATE LIKE ROW AND COLUMN LABELS:
        letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # DICTIONARY TO STORE ALL PLACES THAT ARE HIT AND OR MISSED WITH A SPECIFIC KEY
        self.attack_dict = {}

        # LIST TO STORE COORDINATES OF GRID
        self.cord_list = []

        # DICTIONARY TO APPEND COORDINATES TO BUTTONS CREATED
        self.buttons_dict = {}

        # MAIN FRAME SETUP:
        self.board_frame = tk.Tk()
        self.board_frame.title("AI Board")
        self.board_frame.geometry("550x550")
        self.attack_entry = tk.Entry(self.board_frame, bg="white", fg="black")
        self.attack_lbl = tk.Label(self.board_frame, bg="white", fg="black", text="Guess: ")
        self.attack_btn = tk.Button(self.board_frame, bg="black", fg="white", text="Enter")

        # PROGRESS BAR
        self.progress_bar = ttk.Progressbar(self.board_frame, orient=HORIZONTAL, length=300, mode='determinate')

        # MAIN FRAME FOR USER BOARD
        for grid_row in range(50, 550, 50):
            for grid_col in range(50, 550, 50):
                self.coord = str(grid_row) + "_" + str(grid_col)
                self.cord_list.append(self.coord)
                self.buttons_dict[self.cord_list[-1]] = tk.Button(self.board_frame, bg="blue",
                                                                  text=" ")
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

    # METHOD TO GENERATE COORDINATES FOR SHIP PLACEMENT
    def random_ship_coord(self):
        # STORES ORIENTATION OF SHIP
        orientation = randrange(0, 2, 1)
        # STORES COLUMN AND ROW COORDINATES FOR SHIP
        row = randrange(50, 550, 50)
        col = randrange(50, 550, 50)
        return row, col, orientation

    # METHOD TO INVOKE SHIP PLACEMENT FO AI
    def place_ships(self):
        time.sleep(1)
        self.place_carrier()
        self.place_battleship()
        self.place_cruiser()
        self.place_submarine()
        self.place_destroyer()

    # METHOD TO PLACE SHIPS ON BOARD
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

    # METHOD TO PLACE CARRIER SHIP GIVEN RANDOM COORDINATES
    def place_carrier(self):

        board_row = self.random_ship_coord()[0]
        board_col = self.random_ship_coord()[1]
        orientation = self.random_ship_coord()[2]

        # CHECK HORIZONTAL AND VERTICAL OUT OF BOUNDS TO REASSIGN COORDINATE VARIABLES
        while orientation == 1 and board_row >= 300 or (orientation == 0 and board_col >= 300):
            board_row = self.random_ship_coord()[0]
            board_col = self.random_ship_coord()[1]
            if orientation == 1 and board_row <= 300 or (orientation == 0 and board_col <= 300):
                break

        # PLACES CARRIER SHIP HORIZONTALLY
        if orientation == 1 and board_row <= 300:
            self.placing_ships(board_row, board_col, orientation, "green", 4)

        # PLACES CARRIER SHIP VERTICALLY
        elif orientation == 0 and board_col <= 300:
            self.placing_ships(board_row, board_col, orientation, "green", 4)

    # METHOD TO PLACE BATTLESHIP SHIP GIVEN RANDOM COORDINATES
    def place_battleship(self):

        board_row = self.random_ship_coord()[0]
        board_col = self.random_ship_coord()[1]
        orientation = self.random_ship_coord()[2]

        # CHECK HORIZONTAL AND VERTICAL OUT OF BOUNDS TO REASSIGN COORDINATE VARIABLES
        while orientation == 1 and board_row >= 350 or (orientation == 0 and board_col >= 350):
            board_row = self.random_ship_coord()[0]
            board_col = self.random_ship_coord()[1]
            if orientation == 1 and board_row <= 350 or (orientation == 0 and board_col <= 350):
                break

        # PLACES BATTLESHIP SHIP HORIZONTALLY
        if orientation == 1 and board_row <= 350:

            # CHECK FOR SHIP OCCUPATION
            while self.buttons_dict[f'{board_row}_{board_col}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row + 50}_{board_col}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row + 100}_{board_col}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row + 150}_{board_col}'].cget("text") != " ":
                board_row = self.random_ship_coord()[0]
                board_col = self.random_ship_coord()[1]
                while board_row >= 350 or board_col >= 350:
                    board_row = self.random_ship_coord()[0]
                    board_col = self.random_ship_coord()[1]
                    if board_row <= 350 and board_col <= 350:
                        break
                if self.buttons_dict[f'{board_row}_{board_col}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row + 50}_{board_col}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row + 100}_{board_col}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row + 150}_{board_col}'].cget("text") == " ":
                    break
            self.placing_ships(board_row, board_col, orientation, "yellow", 3)

        # PLACES BATTLESHIP SHIP VERTICALLY
        elif orientation == 0 and board_col <= 350:

            # CHECK FOR SHIP OCCUPATION
            while self.buttons_dict[f'{board_row}_{board_col}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row}_{board_col + 50}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row}_{board_col + 100}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row}_{board_col + 150}'].cget("text") != " ":
                board_row = self.random_ship_coord()[0]
                board_col = self.random_ship_coord()[1]
                while board_row >= 350 or board_col >= 350:
                    board_row = self.random_ship_coord()[0]
                    board_col = self.random_ship_coord()[1]
                    if board_row <= 350 and board_col <= 350:
                        break
                if self.buttons_dict[f'{board_row}_{board_col}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row}_{board_col + 50}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row}_{board_col + 100}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row}_{board_col + 150}'].cget("text") == " ":
                    break
            self.placing_ships(board_row, board_col, orientation, "yellow", 3)

    # METHOD TO PLACE CRUISER SHIP GIVEN RANDOM COORDINATES
    def place_cruiser(self):

        board_row = self.random_ship_coord()[0]
        board_col = self.random_ship_coord()[1]
        orientation = self.random_ship_coord()[2]

        # CHECK HORIZONTAL AND VERTICAL OUT OF BOUNDS TO REASSIGN COORDINATE VARIABLES
        while orientation == 1 and board_row >= 400 or (orientation == 0 and board_col >= 400):
            board_row = self.random_ship_coord()[0]
            board_col = self.random_ship_coord()[1]
            if orientation == 1 and board_row <= 400 or (orientation == 0 and board_col <= 400):
                break

        # PLACES CRUISER SHIP HORIZONTALLY
        if orientation == 1 and board_row <= 400:

            # CHECK FOR SHIP OCCUPATION
            while self.buttons_dict[f'{board_row}_{board_col}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row + 50}_{board_col}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row + 100}_{board_col}'].cget("text") != " ":
                board_row = self.random_ship_coord()[0]
                board_col = self.random_ship_coord()[1]
                while board_row >= 400 or board_col >= 400:
                    board_row = self.random_ship_coord()[0]
                    board_col = self.random_ship_coord()[1]
                    if board_row <= 400 and board_col <= 400:
                        break
                if self.buttons_dict[f'{board_row}_{board_col}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row + 50}_{board_col}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row + 100}_{board_col}'].cget("text") == " ":
                    break
            self.placing_ships(board_row, board_col, orientation, "orange", 2)

        # PLACES CRUISER SHIP VERTICALLY
        elif orientation == 0 and board_col <= 400:

            # CHECK FOR SHIP OCCUPATION
            while self.buttons_dict[f'{board_row}_{board_col}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row}_{board_col + 50}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row}_{board_col + 100}'].cget("text") != " ":
                board_row = self.random_ship_coord()[0]
                board_col = self.random_ship_coord()[1]
                while board_row >= 400 or board_col >= 400:
                    board_row = self.random_ship_coord()[0]
                    board_col = self.random_ship_coord()[1]
                    if board_row <= 400 and board_col <= 400:
                        break
                if self.buttons_dict[f'{board_row}_{board_col}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row}_{board_col + 50}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row}_{board_col + 100}'].cget("text") == " ":
                    break
            self.placing_ships(board_row, board_col, orientation, "orange", 2)

    # METHOD TO PLACE SUBMARINE SHIP GIVEN RANDOM COORDINATES
    def place_submarine(self):

        board_row = self.random_ship_coord()[0]
        board_col = self.random_ship_coord()[1]
        orientation = self.random_ship_coord()[2]

        # CHECK HORIZONTAL AND VERTICAL OUT OF BOUNDS TO REASSIGN COORDINATE VARIABLES
        while orientation == 1 and board_row > 400 or (orientation == 0 and board_col > 400):
            board_row = self.random_ship_coord()[0]
            board_col = self.random_ship_coord()[1]
            if orientation == 1 and board_row <= 400 or (orientation == 0 and board_col <= 400):
                break

        # PLACES SUBMARINE SHIP HORIZONTALLY
        if orientation == 1 and board_row <= 400:

            # CHECK FOR SHIP OCCUPATION
            while self.buttons_dict[f'{board_row}_{board_col}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row + 50}_{board_col}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row + 100}_{board_col}'].cget("text") != " ":
                board_row = self.random_ship_coord()[0]
                board_col = self.random_ship_coord()[1]
                while board_row >= 400 or board_col >= 400:
                    board_row = self.random_ship_coord()[0]
                    board_col = self.random_ship_coord()[1]
                    if board_row <= 400 and board_col <= 400:
                        break
                if self.buttons_dict[f'{board_row}_{board_col}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row + 50}_{board_col}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row + 100}_{board_col}'].cget("text") == " ":
                    break
            self.placing_ships(board_row, board_col, orientation, "red", 2)

        # PLACES SUBMARINE SHIP VERTICALLY
        elif orientation == 0 and board_col <= 400:

            # CHECK FOR SHIP OCCUPATION
            while self.buttons_dict[f'{board_row}_{board_col}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row}_{board_col + 50}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row}_{board_col + 100}'].cget("text") != " ":
                board_row = self.random_ship_coord()[0]
                board_col = self.random_ship_coord()[1]
                while board_row >= 400 or board_col >= 400:
                    board_row = self.random_ship_coord()[0]
                    board_col = self.random_ship_coord()[1]
                    if board_row <= 400 and board_col <= 400:
                        break
                if self.buttons_dict[f'{board_row}_{board_col}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row}_{board_col + 50}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row}_{board_col + 100}'].cget("text") == " ":
                    break
            self.placing_ships(board_row, board_col, orientation, "red", 2)

    # METHOD TO PLACE DESTROYER SHIP GIVEN RANDOM COORDINATES
    def place_destroyer(self):

        board_row = self.random_ship_coord()[0]
        board_col = self.random_ship_coord()[1]
        orientation = self.random_ship_coord()[2]

        # CHECK HORIZONTAL AND VERTICAL OUT OF BOUNDS TO REASSIGN COORDINATE VARIABLES
        while orientation == 1 and board_row > 450 or (orientation == 0 and board_col > 450):
            board_row = self.random_ship_coord()[0]
            board_col = self.random_ship_coord()[1]
            if orientation == 1 and board_row <= 450 or (orientation == 0 and board_col <= 450):
                break

        # PLACES DESTROYER SHIP HORIZONTALLY
        if orientation == 1 and board_row <= 450:

            # CHECK FOR SHIP OCCUPATION
            while self.buttons_dict[f'{board_row}_{board_col}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row + 50}_{board_col}'].cget("text") != " ":
                board_row = self.random_ship_coord()[0]
                board_col = self.random_ship_coord()[1]
                while board_row > 450 or board_col > 450:
                    board_row = self.random_ship_coord()[0]
                    board_col = self.random_ship_coord()[1]
                    if board_row <= 450 and board_col <= 450:
                        break
                if self.buttons_dict[f'{board_row}_{board_col}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row + 50}_{board_col}'].cget("text") == " ":
                    break
            self.placing_ships(board_row, board_col, orientation, "purple", 1)

        # PLACES DESTROYER SHIP VERTICALLY
        elif orientation == 0 and board_col <= 450:

            # CHECK FOR SHIP OCCUPATION
            while self.buttons_dict[f'{board_row}_{board_col}'].cget("text") != " " \
                    or self.buttons_dict[f'{board_row}_{board_col + 50}'].cget("text") != " ":
                board_row = self.random_ship_coord()[0]
                board_col = self.random_ship_coord()[1]
                while board_row > 450 or board_col > 450:
                    board_row = self.random_ship_coord()[0]
                    board_col = self.random_ship_coord()[1]
                    if board_row <= 450 and board_col <= 450:
                        break
                if self.buttons_dict[f'{board_row}_{board_col}'].cget("text") == " " \
                        and self.buttons_dict[f'{board_row}_{board_col + 50}'].cget("text") == " ":
                    break
            self.placing_ships(board_row, board_col, orientation, "purple", 1)
