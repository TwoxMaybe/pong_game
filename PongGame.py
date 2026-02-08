import time
from turtle import Screen
from player import Player
from ball import Ball
from game_constants import (VERTICAL_RIGHT_LIMIT_TO_SCORE, VERTICAL_lEFT_LIMIT_TO_SCORE,
                            SCORE_TO_WIN,
                            X_COR_PLAYER1, X_COR_PLAYER2,
                            X_COR_SCOREBOARD1, X_COR_SCOREBOARD2, Y_COR_SCOREBOARD12,
                            WIDTH_SCREEN, HEIGHT_SCREEN)

class PongGame:
    """
    Manages the main game logic, loop, and object interactions for Pong.

    This class initializes the game window, the game entities (players, ball),
    handles input controls, manages collisions, and controls the game flow.
    """

    def __init__(self) -> None:
        """
        Initialize the PongGame instance.

        Sets up the screen, creates the players and ball objects,
        configures the controls, and initializes the game state variable.
        """
        # Screen configuration
        self.screen = Screen()
        self.initialize_screen()

        # Objects configuration
        self.player1 = Player(X_COR_SCOREBOARD1, Y_COR_SCOREBOARD12, X_COR_PLAYER1)
        self.player2 = Player(X_COR_SCOREBOARD2, Y_COR_SCOREBOARD12, X_COR_PLAYER2)
        self.ball = Ball()

        # Control configuration
        self.activate_control()

        # Loop flow control variable
        self.is_game_running: bool = True

    def initialize_screen(self) -> None:
        """
        Configure the main game window settings.

        Sets the dimensions, title, background color, and turns off
        automatic animation (tracer) for manual update control.
        """
        self.screen.setup(WIDTH_SCREEN, HEIGHT_SCREEN)
        self.screen.title("Pong Game")
        self.screen.bgcolor("black")
        self.screen.tracer(0)

    def activate_control(self) -> None:
        """
        Bind keyboard keys to player movement methods.

        Sets up event listeners for 'w'/'s' (Player 1) and Arrow Keys (Player 2).
        """
        self.screen.listen()

        # Player 1 Controls
        self.screen.onkeypress(self.player1.press_up, "w")
        self.screen.onkeyrelease(self.player1.off_up, "w")

        self.screen.onkeypress(self.player1.press_down, "s")
        self.screen.onkeyrelease(self.player1.off_down, "s")

        # Player 2 Controls
        self.screen.onkeypress(self.player2.press_up, "Up")
        self.screen.onkeyrelease(self.player2.off_up, "Up")

        self.screen.onkeypress(self.player2.press_down, "Down")
        self.screen.onkeyrelease(self.player2.off_down, "Down")

    def check_if_is_point(self) -> None:
        """
        Check if the ball has passed a player's paddle to award a point.

        If the ball goes beyond the left or right vertical limits,
        a point is given to the opposing player, and the ball is reset.
        """
        # The ball is behind Player 1 (Left side)
        if self.ball.xcor() < VERTICAL_lEFT_LIMIT_TO_SCORE:
            self.player2.give_point()
            self.ball.move_to_origin()

        # The ball is behind Player 2 (Right side)
        elif self.ball.xcor() > VERTICAL_RIGHT_LIMIT_TO_SCORE:
            self.player1.give_point()
            self.ball.move_to_origin()

    def is_game_over(self) -> bool:
        """
        Check if the winning condition has been met.

        Returns:
            bool: True if a player has reached the SCORE_TO_WIN, False otherwise.
        """
        actual_high_score = max(self.player1.get_score(), self.player2.get_score())

        if actual_high_score == SCORE_TO_WIN:
            return True

        return False

    def start_game(self) -> None:
        """
        Run the main game loop.

        Handles screen updates, object movement, collision detection,
        scoring checks, and the game over condition.
        """
        while self.is_game_running:

            # Display scores
            self.player1.show_score()
            self.player2.show_score()

            # Move the ball and check for collisions
            time.sleep(0.01)
            self.ball.move()
            self.player1.move_player()
            self.player2.move_player()
            self.handle_collisions(self.player1, self.player2)

            # Update the screen to show changes
            self.screen.update()

            # Check if game should continue
            game_is_on = not self.is_game_over()
            if not game_is_on:
                self.is_game_running = False

            # Check for scoring
            self.check_if_is_point()

        # Show game over message
        self.player1.show_end_game()
        self.screen.exitonclick()

    def handle_collisions(self, player1: Player, player2: Player) -> None:
        """
        Detect and resolve collisions between the ball, walls, and players.

        Args:
            player1 (Player): The left-side player object.
            player2 (Player): The right-side player object.
        """
        # Bounce off top and bottom borders
        if self.ball.is_crash_with_borders():
            self.ball.bounce_y()

        # Collision with Player 1 (Left)
        elif self.ball.is_crash_with_player(player1) and self.ball.x_move < 0:
            self.ball.bounce_x()
            # Slight offset to prevent ball getting stuck inside paddle
            self.ball.setx(player1.get_x_position() + 10)

        # Collision with Player 2 (Right)
        elif self.ball.is_crash_with_player(player2) and self.ball.x_move > 0:
            self.ball.bounce_x()
            # Slight offset to prevent ball getting stuck inside paddle
            self.ball.setx(player2.get_x_position() - 10)