from turtle import Turtle
from game_constants import HEIGHT_SCREEN, BAR_MOVEMENT_SPEED

# Constants for direction
UP = 90
DOWN = 270


class Bar(Turtle):
    """
    Represents a player's paddle (bar) in the Pong game.

    Inherits from the Turtle class to handle graphical representation and movement.
    It uses a flag-based system for movement to allow smooth control responsiveness.
    """

    def __init__(self, x_cor: float) -> None:
        """
        Initialize the Bar object at a specific x-coordinate.

        Args:
            x_cor (float): The initial x-coordinate for the bar.
        """
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.setheading(90)
        self.color("white")
        self.setposition(x_cor, 0)

        # Dictionary to track the state of movement keys
        self.directions: dict[str, bool] = {"UP": False, "DOWN": False}

    def press_up(self) -> None:
        """Set the 'UP' movement flag to True."""
        self.directions["UP"] = True

    def off_up(self) -> None:
        """Set the 'UP' movement flag to False (key released)."""
        self.directions["UP"] = False

    def press_down(self) -> None:
        """Set the 'DOWN' movement flag to True."""
        self.directions["DOWN"] = True

    def off_down(self) -> None:
        """Set the 'DOWN' movement flag to False (key released)."""
        self.directions["DOWN"] = False

    def move(self) -> None:
        """
        Move the bar based on the current direction flags.

        Checks the boundaries of the screen to prevent the bar from moving
        outside the playable area. If a movement key is active and the
        bar is within limits, it updates the position.
        """
        if self.directions["UP"]:
            # Check upper boundary
            if self.position()[1] >= (HEIGHT_SCREEN / 2) - 40:
                return

            self.setheading(UP)
            self.forward(BAR_MOVEMENT_SPEED)

        elif self.directions["DOWN"]:
            # Check lower boundary
            if self.position()[1] <= -1 * ((HEIGHT_SCREEN / 2) - 40):
                return

            self.setheading(DOWN)
            self.forward(BAR_MOVEMENT_SPEED)