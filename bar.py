from turtle import Turtle
from game_constants import (HEIGHT_SCREEN,
                            BAR_MOVEMENT_SPEED)

#Constants
UP = 90
DOWN = 270

class Bar(Turtle):
    def __init__(self, x_cor) -> None:
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.setheading(90)
        self.color("white")
        self.setposition(x_cor,0)
        self.directions ={"UP": False, "DOWN": False}

    def press_up(self): self.directions["UP"] = True

    def off_up(self): self.directions["UP"] = False

    def press_down(self): self.directions["DOWN"] = True

    def off_down(self): self.directions["DOWN"] = False

    def move(self):
        if self.directions["UP"]:
            if self.position()[1] >= (HEIGHT_SCREEN/2) - 40:
                return

            self.setheading(UP)
            self.forward(BAR_MOVEMENT_SPEED)

        elif self.directions["DOWN"]:
            if self.position()[1] <= -1 * ((HEIGHT_SCREEN/2) - 40):
                return

            self.setheading(DOWN)
            self.forward(BAR_MOVEMENT_SPEED)

        return



