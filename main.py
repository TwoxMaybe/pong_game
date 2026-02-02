from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import check_if_is_point, is_game_over
import game_constants as const
import time

#Screen configuration
screen = Screen()
screen.setup(const.WIDTH_SCREEN, const.HEIGHT_SCREEN)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0) #Off automatic animations

#Objects configuration
player1 = Player( -1 * const.X_COR_SCOREBOARD, const.Y_COR_SCOREBOARD, -1 * const.X_COR_PLAYER)
player2 = Player(const.X_COR_SCOREBOARD, const.Y_COR_SCOREBOARD, const.X_COR_PLAYER)
ball = Ball()

# Controls keys configurations
screen.listen()

#Player 1
screen.onkeypress(player1.move_up, "w")
screen.onkeypress(player1.move_down, "s")

#PLayer 2
screen.onkeypress(player2.move_up, "Up")
screen.onkeypress(player2.move_down, "Down")

#Variable of control
game_is_on = True

while game_is_on:

    #Muestra los marcadores
    player1.show_score()
    player2.show_score()

    #Mueva la pelota y verifique si no ha chocado
    time.sleep(0.1)
    ball.move()

    #Actualiza la pantalla para mostrar los cambios
    screen.update()

    #Casos de anotación:
    check_if_is_point(ball,player1,player2)

    #Casos donde se termina el juego
    game_is_on = is_game_over(player1,player2)

#Mostrar mensaje de juego acabado
#Cualquiera puede mostrar quien es el que perdió, es indiferente para la logica
player1.show_end_game()
screen.exitonclick()

