from turtle import Screen
from player import Player
from ball import Ball
from game_constants import VERTICAL_RIGHT_LIMIT_TO_SCORE, VERTICAL_lEFT_LIMIT_TO_SCORE, SCORE_TO_WIN
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

#Functions

def check_if_is_point():

    # Se obtiene un punto cuando la bola supera la posición de la barra en x
    if ball.pos()[0] < VERTICAL_lEFT_LIMIT_TO_SCORE:
        player2.give_point()
        ball.move_to_origin()

    elif ball.pos()[0] > VERTICAL_RIGHT_LIMIT_TO_SCORE:
        player1.give_point()
        ball.move_to_origin()

    return
def is_game_over():

    same_score = player1.get_score() == player2.get_score() == SCORE_TO_WIN
    actual_high_score = max(player1.get_score(), player2.get_score())

    # Si ambos alcanzan el mismo marcador
    if same_score:
        actual_score_diff = abs(player1.get_score() - player2.get_score())
        diff_of_two = actual_score_diff == 2

        if diff_of_two:
            return False

    # El primero en alcanzar el marcador decidido
    elif actual_high_score == SCORE_TO_WIN:
        return False

    return True

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
    ball.is_crash(player1,player2)


    #Actualiza la pantalla para mostrar los cambios
    screen.update()

    #Casos de anotación:
    check_if_is_point()

    #Casos donde se termina el juego
    game_is_on = is_game_over()

#Mostrar mensaje de juego acabado
#Cualquiera puede mostrar quien es el que perdió, es indiferente para la logica
player1.show_end_game()
screen.exitonclick()

