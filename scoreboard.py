from turtle import Turtle

class Scoreboard(Turtle):
    """
    Handles the display and tracking of a player's score.

    Inherits from the Turtle class to draw the score and game over messages
    on the screen.
    """

    def __init__(self, x_cor: float, y_cor: float) -> None:
        """
        Initialize the Scoreboard at a specific position.

        Args:
            x_cor (float): The x-coordinate for the scoreboard.
            y_cor (float): The y-coordinate for the scoreboard.
        """
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(x_cor, y_cor)
        self.color("white")
        self.score: int = 0

    def add_point(self) -> None:
        """Increment the current score by one."""
        self.score += 1

    def show_score(self) -> None:
        """
        Clear the previous score and write the current score on the screen.

        Uses the current position and a specific font style to display the score.
        """
        self.clear()
        self.write(str(self.score), False, "center", ("Arial", 18, "normal"))

    def show_end_game(self) -> None:
        """
        Display the 'Game Over' message at the center of the screen.

        Moves the turtle to the center (0, 0) before writing.
        """
        self.setposition(0, 0)
        self.write("Game Over", False, "center", ("Arial", 18, "normal"))

    def get_score(self) -> int:
        """
        Retrieve the current score.

        Returns:
            int: The current score value.
        """
        return self.score