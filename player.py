from scoreboard import Scoreboard
from bar import Bar

class Player:
    def __init__(self, x_cor_scoreboard, y_cor_scoreboard, x_cor_bar):
        self.scoreboard = Scoreboard(x_cor_scoreboard, y_cor_scoreboard)
        self.bar = Bar(x_cor_bar)

    def show_score(self):
        self.scoreboard.show_score()
        return

    def move_up(self):
        self.bar.up()
        return

    def move_down(self):
        self.bar.down()
        return

    def show_end_game(self):
        self.scoreboard.show_end_game()
        return

    def get_score(self):
        return self.scoreboard.get_score()

