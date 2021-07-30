        
    def guess_after_miss(self):
        self.attack_counter = self.attack_counter + 1
        row_guess = randrange(250, 550, 50)
        col_guess = randrange(250, 550, 50)
        if self.buttons_dict[f'{row_guess}_{col_guess}'].cget("text") == "   ":
            self.buttons_dict[f'{row_guess}_{col_guess}'].configure(state=DISABLED, bg="black", text="HIT")
            self.win_counter = self.win_counter + 1
            self.educated_hit_guess(row_guess, col_guess)
        elif self.buttons_dict[f'{row_guess}_{col_guess}'].cget("bg") == "blue":
            self.buttons_dict[f'{row_guess}_{col_guess}'].configure(state=DISABLED, bg="white", text="MISS")
            self.guess_after_miss()
        elif self.buttons_dict[f'{row_guess}_{col_guess}'].cget("text") == "MISS":
            self.attack_counter = self.attack_counter - 1
            self.guess_after_miss()
