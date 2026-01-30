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

    #Se debe de limitar que las barras no traspasen el marco
    def up(self):
        if self.position()[1] >= 260 :
            return

        self.setheading(UP)
        self.forward(10)
        return

    def down(self):

        if self.position()[1] <= -250:
            return

        self.setheading(DOWN)
        self.forward(20)
        return


