import time
from turtle import Screen
from player import Player
from ball import Ball
from game_constants  import (VERTICAL_RIGHT_LIMIT_TO_SCORE, VERTICAL_lEFT_LIMIT_TO_SCORE,
                             SCORE_TO_WIN,
                             X_COR_PLAYER1, X_COR_PLAYER2,
                             X_COR_SCOREBOARD1, X_COR_SCOREBOARD2, Y_COR_SCOREBOARD12,
                             WIDTH_SCREEN, HEIGHT_SCREEN)


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

    actual_high_score = max(player1.get_score(), player2.get_score())

    # Si ambos alcanzan el mismo marcador
    if actual_high_score == SCORE_TO_WIN:
        return True

    return False

#Screen configuration
screen = Screen()
screen.setup(WIDTH_SCREEN, HEIGHT_SCREEN)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

#Objects configuration
player1 = Player(X_COR_SCOREBOARD1, Y_COR_SCOREBOARD12, X_COR_PLAYER1)
player2 = Player(X_COR_SCOREBOARD2, Y_COR_SCOREBOARD12, X_COR_PLAYER2)
ball = Ball()

# Controls keys configurations
screen.listen()

#Player 1
screen.onkeypress(player1.press_up, "w")
screen.onkeyrelease(player1.off_up, "w")

screen.onkeypress(player1.press_down, "s")
screen.onkeyrelease(player1.off_down, "s")

#PLayer 2
screen.onkeypress(player2.press_up, "Up")
screen.onkeyrelease(player2.off_up, "Up")

screen.onkeypress(player2.press_down, "Down")
screen.onkeyrelease(player2.off_down, "Down")

#Variable of control
game_is_on = True

while game_is_on:

    #Muestra los marcadores
    player1.show_score()
    player2.show_score()

    #Mueva la pelota y verifique si no ha chocado
    time.sleep(0.01)
    ball.move()
    player1.move_player()
    player2.move_player()
    ball.is_crash(player1,player2)

    #Actualiza la pantalla para mostrar los cambios
    screen.update()

    #Casos donde se termina el juego
    game_is_on = not is_game_over()

    #Casos de anotación:
    check_if_is_point()

#Mostrar mensaje de juego acabado
player1.show_end_game()
screen.exitonclick()

