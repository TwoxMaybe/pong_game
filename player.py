from scoreboard import Scoreboard
from bar import Bar

class Player:
    """
    Represents a player in the Pong game.

    This class acts as a facade, managing both the player's paddle (Bar)
    and their score (Scoreboard). It delegates movement and scoring
    operations to these internal components.
    """

    def __init__(self, x_cor_scoreboard: float, y_cor_scoreboard: float, x_cor_bar: float) -> None:
        """
        Initialize the Player object with a paddle and a scoreboard.

        Args:
            x_cor_scoreboard (float): The x-coordinate for the player's scoreboard.
            y_cor_scoreboard (float): The y-coordinate for the player's scoreboard.
            x_cor_bar (float): The initial x-coordinate for the player's paddle.
        """
        self.scoreboard = Scoreboard(x_cor_scoreboard, y_cor_scoreboard)
        self.bar = Bar(x_cor_bar)

    def get_y_position(self) -> float:
        """
        Get the current vertical position of the player's paddle.

        Returns:
            float: The y-coordinate of the paddle.
        """
        return self.bar.position()[1]

    def get_x_position(self) -> float:
        """
        Get the current horizontal position of the player's paddle.

        Returns:
            float: The x-coordinate of the paddle.
        """
        return self.bar.position()[0]

    def move_player(self) -> None:
        """Update the position of the player's paddle based on input."""
        self.bar.move()

    def press_up(self) -> None:
        """Handle the input to move the paddle up."""
        self.bar.press_up()

    def off_up(self) -> None:
        """Handle the release of the up input key."""
        self.bar.off_up()

    def press_down(self) -> None:
        """Handle the input to move the paddle down."""
        self.bar.press_down()

    def off_down(self) -> None:
        """Handle the release of the down input key."""
        self.bar.off_down()

    def get_score(self) -> int:
        """
        Get the player's current score.

        Returns:
            int: The current score.
        """
        return self.scoreboard.get_score()

    def give_point(self) -> None:
        """Increment the player's score by one point."""
        self.scoreboard.add_point()

    def show_score(self) -> None:
        """Display the current score on the screen."""
        self.scoreboard.show_score()

    def show_end_game(self) -> None:
        """Display the 'Game Over' message."""
        self.scoreboard.show_end_game()

