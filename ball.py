from turtle import Turtle
from typing import Any
import random
from game_constants import (HEIGHT_SCREEN, MAX_SPEED,
                            COLISSION_DISTANCE_X, COLISSION_DISTANCE_Y,
                            BALL_INITIAL_SPEED)

class Ball(Turtle):
    """
    Represents the ball in the Pong game.

    Inherits from the Turtle class and handles its own movement, collision checks
    with borders and players, and speed adjustments.
    """

    def __init__(self) -> None:
        """
        Initialize the Ball object.

        Sets up the graphical appearance, initial position, speed, and
        movement vectors.
        """
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setposition(0, 0)
        self.penup()
        self.possible_directions: list[int] = [0, 45, 135, 225, 315]
        self.direction: int = 0
        self.speed(1)

        # Initial movement vectors (will become floats when multiplied by speed factor)
        self.x_move: float = 3
        self.y_move: float = 3
        self.speed_factor: float = BALL_INITIAL_SPEED

    def random_direction(self) -> int:
        """
        Choose a random direction from the possible directions list.

        Returns:
            int: The chosen direction in degrees.
        """
        self.direction = random.choice(self.possible_directions)
        return self.direction

    def is_crash_with_borders(self) -> bool:
        """
        Check if the ball has collided with the top or bottom screen borders.

        Returns:
            bool: True if a collision occurred, False otherwise.
        """
        top_border_pos = (HEIGHT_SCREEN / 2) - 10
        low_border_pos = -1 * ((HEIGHT_SCREEN / 2) - 10)

        if self.position()[1] >= top_border_pos  or self.position()[1] <= low_border_pos :
            return True
        return False

    def is_crash_with_player(self, player: Any) -> bool:
        """
        Check if the ball has collided with a player's paddle.

        Args:
            player (Any): The player object to check collision against.
                          Expected to have get_x_position() and get_y_position() methods.

        Returns:
            bool: True if collision criteria (distance X and Y) are met in the defined interval, False otherwise.
        """
        x_pos_diff = abs(self.position()[0] - player.get_x_position())
        y_pos_diff = abs(self.position()[1] - player.get_y_position())

        collision_y = y_pos_diff <= COLISSION_DISTANCE_Y
        collision_x = x_pos_diff <= COLISSION_DISTANCE_X

        is_crash = collision_x and collision_y

        if is_crash:
            return True

        return False

    def move(self) -> None:
        """
        Update the ball's position based on its current movement vectors.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self) -> None:
        """
        Invert the vertical movement direction (bounce off top/bottom walls).
        """
        self.y_move *= -1

    def bounce_x(self) -> None:
        """
        Invert the horizontal movement direction and increase speed.

        This usually happens when the ball hits a paddle. If the speed
        has not reached MAX_SPEED, it is increased by the speed_factor.
        """
        self.x_move *= -1

        if self.x_move >= MAX_SPEED or self.y_move >= MAX_SPEED:
            return

        self.x_move *= self.speed_factor
        self.y_move *= self.speed_factor

    def move_to_origin(self) -> None:
        """
        Reset the ball to the center of the screen and randomize its direction.

        Used when a point is scored. Resets speed to initial values and
        assigns a random direction.
        """
        self.setposition(0, 0)
        self.direction = self.random_direction()

        self.x_move, self.y_move = 3, 3

        multiplicator = [-1, 1]
        self.x_move *= random.choice(multiplicator)
        self.y_move *= random.choice(multiplicator)

        self.setheading(self.direction)

