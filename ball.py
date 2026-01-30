from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setposition(0,0)
        self.penup()
        self.who_touched = ""

    def get_who_touched(self):
        return self.who_touched

    #Choque contra barras
    #Choque contra pared superior e inferior
    #Caen en la misma categoría de choque

    #Si la bola viene a 45 grados debe reflejarse 45 grados respecto a la pared
    #Si la superficie viene a 90 grados
    #Puede rebotar a 90 grados
    #Puede rebotar a 45 grados





