from turtle import Turtle
import main

#Constants
UP = 90
DOWN = 270

class Bar(Turtle):
    def __init__(self, x_cor) -> None:
        super().__init__()
        self.penup() #Que no deje rastro al moverse
        self.shape("square")
        self.color("white")
        self.setposition(x_cor,0)


    def up(self):
        self.setheading(UP)
        return

    def down(self):
        self.setheading(DOWN)
        return


