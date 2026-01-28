from turtle import Turtle

#Constants
UP = 90
DOWN = 270

class Bar(Turtle):
    def __init__(self, x_cor) -> None:
        super().__init__()
        self.penup() #Que no deje rastro al moverse
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.setheading(90)
        self.color("white")
        self.setposition(x_cor,0)


    def up(self):
        self.setheading(UP)
        self.forward(10)
        return

    def down(self):
        self.setheading(DOWN)
        self.forward(10)
        return


