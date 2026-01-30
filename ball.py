from turtle import Turtle
from main import X_COR_PLAYER
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setposition(0,0)
        self.penup()
        self.who_touched = ""
        self.possible_directions = [45,135,225,315]

    def get_who_touched(self):
        return self.who_touched

    def set_who_touched(self,who_touched):
        self.who_touched = who_touched
        return

    def choose_direction(self):
        return random.choice(self.possible_directions)

    def crash(self):

        #Intervalo en el que se detecta una colisión con le jugador 1
        pos_player1_top = (X_COR_PLAYER + 5,self.position()[1])
        pos_player1_bottom = (X_COR_PLAYER - 5,self.position()[1])

        pos_player2_top = (X_COR_PLAYER - 5, self.position()[1])
        pos_player2_bottom = (X_COR_PLAYER + 5, self.position()[1])

        crash_with_player1 = pos_player1_top >= self.position() >= pos_player1_bottom
        crash_with_player2 = pos_player2_top >= self.position() >= pos_player1_bottom

        # Pared superior o inferior
        if self.position()[1] >= 290 or self.position()[1] < -1 * 290:
            return True

        #A las barras
        elif crash_with_player1 or crash_with_player2:
            return True

        return None


    #def move(self,direction):
     #   self.heading(direction)
      #  while




    #Choque contra barras
    #Choque contra pared superior e inferior
    #Caen en la misma categoría de choque

    #Si la bola viene a 45 grados debe reflejarse 45 grados respecto a la pared
    #Si la superficie viene a 90 grados
    #Puede rebotar a 90 grados
    #Puede rebotar a 45 grados





