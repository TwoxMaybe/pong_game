from turtle import Turtle
from game_constants import (HEIGHT_SCREEN, MAX_SPEED,
                            COLISSION_DISTANCE_X, COLISSION_DISTANCE_Y,
                            BALL_INITIAL_SPEED)
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setposition(0,0)
        self.penup()
        self.possible_directions = [0,45,135,225,315]
        self.direction = 0
        self.speed(1)
        self.x_move, self.y_move = 3, 3
        self.speed_factor = BALL_INITIAL_SPEED

    def random_direction(self):
        self.direction = random.choice(self.possible_directions)
        return self.direction

    def is_crash_with_borders(self):
        if self.position()[1] >= (HEIGHT_SCREEN/2) - 10 or self.position()[1] < -1 * ((HEIGHT_SCREEN/2) - 10):
            return True
        return False

    def is_crash_with_player(self, player):
        x_pos_diff = abs(self.position()[0] - player.get_x_position())
        y_pos_diff = abs(self.position()[1] - player.get_y_position())

        collision_y = y_pos_diff <= COLISSION_DISTANCE_Y
        collision_x = x_pos_diff <= COLISSION_DISTANCE_X

        is_crash =  collision_y and collision_x

        if is_crash:
            return True

        return False

    def handle_collisions(self, player1, player2):

        if self.is_crash_with_borders():
            self.bounce_y()

        elif self.is_crash_with_player(player1) and self.x_move < 0:
            self.bounce_x()
            self.setx(player1.get_x_position() + 10)

        elif self.is_crash_with_player(player2) and self.x_move > 0:
            self.bounce_x()
            self.setx(player2.get_x_position() - 10)

        return

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

        return

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

        if self.x_move >= MAX_SPEED or self.y_move >= MAX_SPEED: return

        self.x_move *= self.speed_factor
        self.y_move *= self.speed_factor

    def move_to_origin(self):
        self.setposition(0,0)
        self.direction = self.random_direction()

        self.x_move,self.y_move = 3,3

        multiplicator = [-1,1]
        self.x_move *=  random.choice(multiplicator)
        self.y_move *=  random.choice(multiplicator)


        self.setheading(self.direction)
        return







