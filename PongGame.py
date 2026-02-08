import time
from turtle import Screen
from player import Player
from ball import Ball
from game_constants  import (VERTICAL_RIGHT_LIMIT_TO_SCORE, VERTICAL_lEFT_LIMIT_TO_SCORE,
                             SCORE_TO_WIN,
                             X_COR_PLAYER1, X_COR_PLAYER2,
                             X_COR_SCOREBOARD1, X_COR_SCOREBOARD2, Y_COR_SCOREBOARD12,
                             WIDTH_SCREEN, HEIGHT_SCREEN)

class PongGame:
    def __init__(self):

        #Screen configuration
        self.screen = Screen()
        self.initialize_screen()

        # Objects configuration
        self.player1 = Player(X_COR_SCOREBOARD1, Y_COR_SCOREBOARD12, X_COR_PLAYER1)
        self.player2 = Player(X_COR_SCOREBOARD2, Y_COR_SCOREBOARD12, X_COR_PLAYER2)
        self.ball = Ball()

        # Control configuration
        self.activate_control()

        #Control variable
        self.is_game_running = True



    def initialize_screen(self):
        self.screen.setup(WIDTH_SCREEN, HEIGHT_SCREEN)
        self.screen.title("Pong Game")
        self.screen.bgcolor("black")
        self.screen.tracer(0)

    def activate_control(self):
        self.screen.listen()

        # Player 1
        self.screen.onkeypress(self.player1.press_up, "w")
        self.screen.onkeyrelease(self.player1.off_up, "w")

        self.screen.onkeypress(self.player1.press_down, "s")
        self.screen.onkeyrelease(self.player1.off_down, "s")

        # PLayer 2
        self.screen.onkeypress(self.player2.press_up, "Up")
        self.screen.onkeyrelease(self.player2.off_up, "Up")

        self.screen.onkeypress(self.player2.press_down, "Down")
        self.screen.onkeyrelease(self.player2.off_down, "Down")

    def check_if_is_point(self) -> None:

        """
        Check if the ball has pass player's position, which
        implies that the ball touched one of the limits
        of the screen (Left or Right)

        """

        if self.ball.xcor() < VERTICAL_lEFT_LIMIT_TO_SCORE:
            self.player2.give_point()
            self.ball.move_to_origin()

        elif self.ball.xcor() > VERTICAL_RIGHT_LIMIT_TO_SCORE:
            self.player1.give_point()
            self.ball.move_to_origin()

    def is_game_over(self) -> bool:
        """
        Check if one of the players has reached the winning score
        """
        actual_high_score = max(self.player1.get_score(), self.player2.get_score())

        if actual_high_score == SCORE_TO_WIN:
            return True

        return False

    def start_game(self):
        while self.is_game_running:

            # Muestra los marcadores
            self.player1.show_score()
            self.player2.show_score()

            # Mueva la pelota y verifique si no ha chocado
            time.sleep(0.01)
            self.ball.move()
            self.player1.move_player()
            self.player2.move_player()
            self.handle_collisions(self.player1, self.player2)

            # Actualiza la pantalla para mostrar los cambios
            self.screen.update()

            # Casos donde se termina el juego
            game_is_on = not self.is_game_over()

            # Casos de anotación:
            self.check_if_is_point()

        # Mostrar mensaje de juego acabado
        self.player1.show_end_game()
        self.screen.exitonclick()

    def handle_collisions(self, player1, player2):

        if self.ball.is_crash_with_borders():
            self.ball.bounce_y()

        elif self.ball.is_crash_with_player(player1) and self.ball.x_move < 0:
            self.ball.bounce_x()
            self.ball.setx(player1.get_x_position() + 10)

        elif self.ball.is_crash_with_player(player2) and self.ball.x_move > 0:
            self.ball.bounce_x()
            self.ball.setx(player2.get_x_position() - 10)

        return

