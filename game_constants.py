"""
This module contains all the global constants used in the Pong game.

It defines screen dimensions, player positions, movement speeds,
collision thresholds, and game rules (like winning score).
Centralizing constants here allows for easy configuration and tuning.
"""

# Screen constants
# Dimensions of the game window in pixels
WIDTH_SCREEN: int = 1200
HEIGHT_SCREEN: int = 600

# Player constants
# Initial X coordinates for Player 2 (Right) and Player 1 (Left)
X_COR_PLAYER2: float = (WIDTH_SCREEN / 2) - 100
X_COR_PLAYER1: float = X_COR_PLAYER2 * -1

# Scoreboard position constants
# Coordinates for placing the score display on the screen
X_COR_SCOREBOARD2: int = 100
X_COR_SCOREBOARD1: int = X_COR_SCOREBOARD2 * -1
Y_COR_SCOREBOARD12: float = (HEIGHT_SCREEN / 2) - 100

# Collision constants
# Threshold distances to detect collision between the ball and paddles
COLISSION_DISTANCE_Y: int = 50
COLISSION_DISTANCE_X: int = 20

# Movement constants
# Speed attributes for the paddle (bar) and the ball
BAR_MOVEMENT_SPEED: int = 10
BALL_INITIAL_SPEED: float = 1.2

# Limits to score constants
# X-axis boundaries; if the ball passes these, a point is scored
VERTICAL_lEFT_LIMIT_TO_SCORE: float = (-1 * (WIDTH_SCREEN / 2)) + 10
VERTICAL_RIGHT_LIMIT_TO_SCORE: float = (WIDTH_SCREEN / 2) - 10

# Game constants
# Rules for game termination and maximum difficulty
SCORE_TO_WIN: int = 10
MAX_SPEED: int = 8