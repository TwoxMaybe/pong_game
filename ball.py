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
        self.possible_directions = [45,135,225,315]
        self.speed(1)

    def get_who_touched(self):
        return self.who_touched

    def set_who_touched(self,who_touched):
        self.who_touched = who_touched
        return

    def choose_direction(self):
        return random.choice(self.possible_directions)

    def crash_with_player(self):

        #Intervalo en el que se detecta una colisión con le jugador 1
        pos_player2_top = (X_COR_PLAYER + 10,self.position()[1] + 40)
        pos_player2_bottom = (X_COR_PLAYER - 10,self.position()[1] - 40)

        pos_player1_top = (-1 * X_COR_PLAYER - 10 , self.position()[1] + 40)
        pos_player1_bottom = (-1 * X_COR_PLAYER + 10, self.position()[1] - 40)

        crash_with_player1 = pos_player1_top >= self.position() >= pos_player1_bottom
        crash_with_player2 = pos_player2_bottom >= self.position() >= pos_player2_top

        # Pared superior o inferior
        if self.position()[1] >= 290 or self.position()[1] < -1 * 290:
            return True

        #A las barras
        elif crash_with_player1:
            self.set_who_touched("1")
            return True

        elif crash_with_player2:
            self.set_who_touched("2")
            return True

        return None


    def move(self):
        if self.crash_with_player():
            new_direction = self.choose_direction()
            self.setheading(new_direction)

        self.forward(20)
        return

    def move_to_origin(self):
        self.setposition(0,0)
        self.setheading(self.choose_direction())
        return







