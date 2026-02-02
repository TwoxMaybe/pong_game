from turtle import Turtle
from game_constants import VERTICAL_RIGHT_LIMIT_TO_SCORE, VERTICAL_lEFT_LIMIT_TO_SCORE, SCORE_TO_WIN

def check_if_is_point(ball, player1, player2):

    # Se obtiene un punto cuando la bola supera la posición de la barra en x
    if ball.pos()[0] < VERTICAL_lEFT_LIMIT_TO_SCORE:
        player2.give_point()
        ball.move_to_origin()

    elif ball.pos()[0] > VERTICAL_RIGHT_LIMIT_TO_SCORE:
        player1.give_point()
        ball.move_to_origin()

    return
def is_game_over(player1,player2):

    same_score = player1.get_score() == player2.get_score() == SCORE_TO_WIN
    actual_high_score = max(player1.get_score(), player2.get_score())

    # Si ambos alcanzan el mismo marcador
    if same_score:
        actual_score_diff = abs(player1.get_score() - player2.get_score())
        diff_of_two = actual_score_diff == 2

        if diff_of_two:
            return False

    # El primero en alcanzar el marcador decidido
    elif actual_high_score == SCORE_TO_WIN:
        return False

    return True


class Scoreboard(Turtle):
    def __init__ (self,x_cor, y_cor) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(x_cor, y_cor)
        self.color("white")
        self.score = 0

    def add_point(self) -> None:
        """Add one point to the score."""
        self.score +=1
        return

    def show_score(self) -> None:
        """Show the actual score"""
        self.clear()
        self.write(str(self.score), False, "center", ("Arial", 18, "normal"))

        return

    def show_end_game(self) -> None:
        """Show the message of the end of the game"""
        self.setposition(0,0)
        self.write("Game Over", False, "center", ("Arial", 18, "normal"))
        return

    def get_score(self):
        return self.score
