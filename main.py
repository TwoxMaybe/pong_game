from turtle import Screen
from Bar import Bar
from scoreboard import Scoreboard

# =================
#Constants:
WIDTH_SCREEN, HEIGHT_SCREEN = 800, 800
X_COR_PLAYER = (WIDTH_SCREEN / 2 ) - 100

#Screen configuration
screen = Screen()
screen.setup(WIDTH_SCREEN, HEIGHT_SCREEN)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0) #Off automatic animations

#Objects configuration
player1 = Bar(X_COR_PLAYER)
player2 = Bar(X_COR_PLAYER)


# Controls keys configurations
screen.listen()

    #Player 1
screen.onkey(player1.up, "Up")
screen.onkey(player1.down, "Down")

    #PLayer 2
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")


#=================
# Data definitions:

# =================
# Functions:
