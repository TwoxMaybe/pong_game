from turtle import Turtle
from game_constants import X_COR_PLAYER
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setposition(0,0)
        self.penup()
        self.who_touched = "1"
        self.possible_directions = [0,45,135,225,315]
        self.direction = 0
        self.speed(1)
        self.x_move, self.y_move = 10, 10

    def get_who_touched(self):
        return self.who_touched

    def set_who_touched(self,who_touched):
        self.who_touched = who_touched
        return

    def random_direction(self):
        self.direction = random.choice(self.possible_directions)
        return self.direction

    def choose_next_direction(self):

        if self.direction == self.possible_directions[0]:
            return self.random_direction()

        elif self.direction == self.possible_directions[1]:
            return self.possible_directions[2]

        elif self.direction == self.possible_directions[2]:
            return self.possible_directions[3]

        elif self.direction == self.possible_directions[3]:
            return self.possible_directions[4]

        return self.possible_directions[0]

    def crash_with_borders(self):

        # Pared superior o inferior
        if self.position()[1] >= 290 or self.position()[1] < -1 * 290:
            return True
        return False

    def crash_with_player(self, player):

        #Si la bola esta lo suficientemente cerca en x y en y se cuenta como choque
        x_pos_diff = abs(self.position()[0] - player.get_x_position())
        y_pos_diff = abs(self.position()[1] - player.get_y_position())

        collision_y = y_pos_diff < 50
        collision_x = x_pos_diff < 20

        is_crash =  collision_y and collision_x

        if is_crash:
            return True

        return False

    def is_crash(self,player1,player2):

        if self.crash_with_borders():
            self.bounce_y()
        elif self.crash_with_player(player1) or self.crash_with_player(player2):
            self.bounce_x()

        return

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

        return

    def bounce_y(self):
        # Invertir dirección vertical (para techos)
        self.y_move *= -1

    def bounce_x(self):
        # Invertir dirección horizontal (para palas)
        self.x_move *= -1

    def move_to_origin(self):
        self.setposition(0,0)
        self.setheading(self.choose_next_direction())
        self.direction = self.random_direction()
        return







