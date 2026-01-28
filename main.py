from turtle import Screen
from player import Player

# =================
#Constants:
WIDTH_SCREEN, HEIGHT_SCREEN = 600, 600
X_COR_PLAYER = (WIDTH_SCREEN / 2 ) - 100

X_COR_SCOREBOARD = 100
Y_COR_SCOREBOARD = (HEIGHT_SCREEN / 2) - 100

SCORE_TO_WIN = 10

#Screen configuration
screen = Screen()
screen.setup(WIDTH_SCREEN, HEIGHT_SCREEN)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0) #Off automatic animations

#Objects configuration
player1 = Player( -1 * X_COR_SCOREBOARD, Y_COR_SCOREBOARD, -1 * X_COR_PLAYER)
player2 = Player(X_COR_SCOREBOARD, Y_COR_SCOREBOARD, X_COR_PLAYER)

# Controls keys configurations
screen.listen()

    #Player 1
screen.onkey(player1.move_up, "w")
screen.onkey(player1.move_down, "s")

    #PLayer 2
screen.onkey(player2.move_up, "Up")
screen.onkey(player2.move_down, "Down")

#Variable of control
game_is_on = True

while game_is_on:

    #Muestra los marcadores
    player1.show_score()
    player2.show_score()

    #Actualiza la pantalla para mostrar los cambios
    screen.update()

    same_score = player1.get_score() == player2.get_score() == SCORE_TO_WIN
    actual_high_score = max(player1.get_score(), player2.get_score())

    #Casos donde se termina el juego
    #Si ambos alcanzan el mismo marcador
    if same_score:
        actual_score_diff = player1.get_score() - player2.get_score()
        diff_of_two = actual_score_diff == 2

        if diff_of_two:
            game_is_on = False

    # El primero en alcanzar el marcador decidido
    if actual_high_score == SCORE_TO_WIN:
        game_is_on = False

#Mostrar mensaje de juego acabado
#Cualquiera puede mostrar quien es el que perdió, es indiferente para la logica
player1.show_end_game()

