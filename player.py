from scoreboard import Scoreboard
from bar import Bar

class Player:
    def __init__(self, x_cor_scoreboard, y_cor_scoreboard, x_cor_bar):
        self.scoreboard = Scoreboard(x_cor_scoreboard, y_cor_scoreboard)
        self.bar = Bar(x_cor_bar)

    def get_y_position(self): return self.bar.position()[1]

    def get_x_position(self): return self.bar.position()[0]

    def move_player(self): self.bar.move()

    def press_up(self): self.bar.press_up()

    def off_up(self): self.bar.off_up()

    def press_down(self): self.bar.press_down()

    def off_down(self): self.bar.off_down()

    def get_score(self): return self.scoreboard.get_score()

    def give_point(self): self.scoreboard.add_point()

    def show_score(self): self.scoreboard.show_score()

    def show_end_game(self): self.scoreboard.show_end_game()








